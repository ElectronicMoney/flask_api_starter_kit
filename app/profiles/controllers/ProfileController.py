from flask import request, jsonify
from app import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app.errors import http_error
from email_validator import validate_email, EmailNotValidError
from app.profiles.schema import profile_schema, profiles_schema
from app.profiles.models.Profile import Profile
from app.auth.Auth import auth
from app.utils import allowed_file
from app.settings import UPLOAD_FOLDER
from werkzeug.utils import secure_filename
import os
import uuid
from flask import send_from_directory
from app.settings import UPLOAD_FOLDER
from app.settings import API_URL


class ProfileController():

    def __init__(self):
        # Init Schema
        self.profile_schema = profile_schema
        self.profiles_schema = profiles_schema
        self.profile = Profile()


    # Get All Users
    def get_all_profiles(self):
        # Check if the user is admin
        if not auth().get('user').is_admin:
            return http_error("You dont' have the permision to Access this resource", 403)
        all_profiles = Profile.query.all()
        all_profiles_result = self.profiles_schema.dump(all_profiles)
        return jsonify(all_profiles_result)
        

    # Get Profile
    def get_profile(self):
        # Check if the authenticated user 
        # is actually the owner of the resource
        user = auth().get('user')

        profile_result = self.profile_schema.dump({
            "name": user.profile.name,
            "profile_picture_url": user.profile.profile_picture_url,
            "profile_created_at": user.profile.profile_created_at,
            "profile_public_id": user.profile.profile_public_id,
            "profile_updated_at": user.profile.profile_updated_at,
            "email": user.email,
            "username": user.username,
            "is_admin": user.is_admin,
            "is_active": user.is_active
        })

        return jsonify(profile_result)


    def upload_profile_picture(self):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return http_error("No file part selected", 400)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                return http_error("No selected file!", 400)

            if file and allowed_file(file.filename):
                # Pass through secure filename
                filename = secure_filename(file.filename)
                # Extract the filename and the file extention
                # file_name, file_ext = os.path.splitext(filename)
                _, file_ext = os.path.splitext(filename)
                # Create a new file_name and concatnate with the ext
                new_file_name = str(uuid.uuid4())
                new_file_name = "{}{}".format(new_file_name, file_ext)

                file.save(os.path.join(UPLOAD_FOLDER, new_file_name))

                # Save the Profile Picture Url in Profile table
                user = auth().get('user') 
                profile = user.profile 
                # Create the Profile Url
                profile_picture_url = "{}{}{}".format(API_URL, '/profile/picture/', new_file_name)
                profile.profile_picture_url = profile_picture_url

                # Then commit the session
                db.session.commit()
                # Return Json Response of the profile to the client
                profile_result = self.profile_schema.dump({
                    "name": profile.name,
                    "profile_picture_url": profile.profile_picture_url,
                    "profile_created_at": profile.profile_created_at,
                    "profile_public_id": profile.profile_public_id,
                    "profile_updated_at": profile.profile_updated_at,
                    "email": user.email,
                    "username": user.username,
                    "is_admin": user.is_admin,
                    "is_active": user.is_active
                })
        
                return self.profile_schema.jsonify(profile_result)

    # Get All Users
    def get_profile_picture(self, filename):
        return send_from_directory(UPLOAD_FOLDER, filename)
        
