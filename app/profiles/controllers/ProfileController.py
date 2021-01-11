from flask import request, jsonify
from app import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app.errors import http_error
from email_validator import validate_email, EmailNotValidError
from app.profiles.schema import profile_schema, profiles_schema
from app.profiles.models.Profile import Profile
from app.auth.Auth import auth


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
            "profile_avatar": user.profile.profile_avatar,
            "profile_created_at": user.profile.profile_created_at,
            "profile_public_id": user.profile.profile_public_id,
            "profile_updated_at": user.profile.profile_updated_at,
            "email": user.email,
            "username": user.username,
            "is_admin": user.is_admin,
            "is_active": user.is_active
        })

        return jsonify(profile_result)
