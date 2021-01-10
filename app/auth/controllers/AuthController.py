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
from werkzeug.security import check_password_hash






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
