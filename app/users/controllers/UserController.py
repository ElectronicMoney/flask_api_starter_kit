from flask import request, jsonify
from app.users.models.User import User
from app.users.schema import user_schema, users_schema
from app import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app.errors import http_error
from email_validator import validate_email, EmailNotValidError
from app.profiles.models.Profile import Profile


class UserController():

    def __init__(self):
        # Init Schema
        self.user_schema = user_schema
        self.users_schema = users_schema
        self.profile = Profile()

    # Create User
    def create_user(self):

        user = User()
        
        # Decode the request data
        data = request.data.decode('utf-8')

        # Check if the first_name is in data
        if 'first_name' in data:
            first_name  = request.json['first_name']
        else:
            return http_error("The First Name is Required!", 400)

        # Check if the first_name is empty
        if not first_name:
           return http_error("The First Name field cannot be empty!", 400)
        else:
            user.first_name  = request.json['first_name']
            

        # Check if the last_name is in data
        if 'last_name' in data:
            last_name  = request.json['last_name']
        else:
            return http_error("The Last Name is Required!", 400)

        # Check if the last_name is empty
        if not last_name:
           return http_error("The Last Name field cannot be empty!", 400)
        else:
            user.last_name  = request.json['last_name']

        
        # Check if the email is in data
        if 'email' in data:
            email  = request.json['email']
        else:
            return http_error("The Email is Required!", 400)

        # Check if the email is empty
        if not email:
           return http_error("The Email field cannot be empty!", 400)

        # Validate the email address
        else:
            email  = request.json['email']
            try:
                # Validate.
                valid = validate_email(email, allow_smtputf8=False)

                # Update with the normalized form.
                user.email  = valid.email
            except EmailNotValidError as e:
                # email is not valid, exception message is human-readable
                return http_error(str(e), 400)
        

        
        # Check if the username is in data
        if 'username' in data:
            username  = request.json['username']
        else:
            return http_error("The Username is Required!", 400)

         # Check the length of the username
        if len(username) < 6:
           return http_error("The Username must be at least 6 characters!", 400)

        # Check if the username is empty
        if not username:
           return http_error("The Username field cannot be empty!", 400)
        else:
            user.username  = request.json['username']

        # Check if the password is in data
        if 'password' in data:
            password  = request.json['password']
        else:
            return http_error("The Password is Required!", 400)

        # Check if the password is empty
        if not password:
           return http_error("The Password field cannot be empty!", 400)

        # Check the length of the password
        if len(password) < 6:
           return http_error("The Password must be at least 6 characters!", 400)
        else:
            password  = request.json['password']
            
        # Hash The Password
        user.password    = generate_password_hash(
            password, 
            method='sha256'
        )

        user.user_public_id   = str(uuid.uuid4())

        # Create Profile Here....
        self.profile.name  = "{} {}".format(user.first_name, user.last_name)
        self.profile.profile_public_id =  str(uuid.uuid4())
        self.profile.user       = user


        # # Add the user to the database
        db.session.add(user)
        # Then commit the session
        db.session.commit()


        # Return Json Response to the client
        return self.user_schema.jsonify(user), 201


    # Get All Users
    def get_all_users(self):
        all_users = User.query.all()
        all_users_result = self.users_schema.dump(all_users)
        return jsonify(all_users_result)
        

    # Get User
    def get_user(self, id):
        user = User.query.filter_by(user_public_id=id).first()
        # Check if not the user
        if not user:
            return http_error("No User Found!", 404)

        user_result = self.user_schema.dump(user)
        return jsonify(user_result)


    # Update User
    def update_user(self, id):
        # get the user you want tot udate
        user = User.query.filter_by(user_id=id).first()

        # Check if not the user
        if not user:
            return http_error("No User Found!", 404)
    
        user.first_name  = request.json['first_name']
        user.last_name   = request.json['last_name']
        user.email       = request.json['email']
        user.username    = request.json['username']

        # Hash The Password
        user.password    = generate_password_hash(
            request.json['password'], 
            method='sha256'
            )

        user.is_admin    = False
        user.is_active   = True
        user.user_id   = str(uuid.uuid4())
        
        # Then commit the session
        db.session.commit()
        # Return Json Response to the client
        return self.user_schema.jsonify(user)



    # Delete User
    def delete_user(self, id):
        user = User.query.query.filter_by(user_id=id).first()
        db.session.delete(user)
        db.session.commit()
        return self.user_schema.jsonify(user)