from flask import request, jsonify
from app import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app.errors import http_error
from email_validator import validate_email, EmailNotValidError
from app.users.models.User import User
from app.auth.schema import auth_schema
import jwt
from app.settings import ACCESS_TOKEN_SECRETE, REFRESH_TOKEN_SECRETE
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.Auth import auth
from app.users.schema import user_schema



class AuthController():

    def __init__(self):
        # Init Schema
        self.auth_schema = auth_schema
        self.secrete_key = ACCESS_TOKEN_SECRETE
        

    # Get User
    def login(self):

        username  = request.json['username']
        password  = request.json['password']

        # Try to get the user using the provided username
        user = User.query.filter_by(email=username).first()
        # Check if not the User
        if not user:
            return http_error("The Username or password is Incorrect!", 401)

        # Check if the user is active
        if not user.is_active:
            return http_error("Authentication Error; Your Account have been suspended!", 401)

        # verify the password
        if not check_password_hash(user.password, password):
            return http_error("The Username or password is Incorrect!", 401)

        # Set the payload; which is the profile
        exp_date = datetime.datetime.utcnow() + datetime.timedelta(hours=24)

        payload = {
            'user': {
                'user_public_id': user.user_public_id
            },
            'exp': exp_date
        } 

        # Emcode the payload using the secrete key
        token = jwt.encode(payload, self.secrete_key, algorithm="HS256")

        auth_token = {"token": token}

        return jsonify(auth_token)

    # Change Password
    def change_password(self):
        # Check if the authenticated user is_admin
        user = auth().get('user')

        # Decode the request data
        data = request.data.decode('utf-8')

         # Check if the Current password is in data
        if 'current_password' in data:
            current_password  = request.json['current_password']
        else:
            return http_error("The Current Password is Required!", 400)

        # Check if the Current password is empty
        if not current_password:
           return http_error("The Current Password field cannot be empty!", 400)

        # verify the Current password
        if not check_password_hash(user.password, current_password):
            return http_error("The Current password you provided is Incorrect!", 400)

        
        # Check if the New password is in data
        if 'new_password' in data:
            new_password  = request.json['new_password']
        else:
            return http_error("The New Password is Required!", 400)

        # Check if the password is empty
        if not new_password:
           return http_error("The New Password field cannot be empty!", 400)
           
        # Check the length of the password
        if len(new_password) < 6:
           return http_error("The New Password must be at least 6 characters!", 400)
        else:
            new_password  = request.json['new_password']

        # Confirm New Pasword
        if 'confirm_new_password' in data:
            confirm_new_password  = request.json['confirm_new_password']
        else:
            return http_error("The Confirm New Password is Required!", 400)
            
        # Check if the confirm New Pasword is the same with the new password
        if new_password != confirm_new_password:
            return http_error("The New Password and confirm new password fields must be the same!", 400)

        # Hash The New Password
        user.password    = generate_password_hash(
            new_password, 
            method='sha256'
        )

       # Then commit the session
        db.session.commit()
        # Return Json Response to the client
        return user_schema.jsonify(user)

