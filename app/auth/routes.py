from flask import Blueprint
from app.auth.controllers.AuthController import AuthController
from app.auth.Auth import check_auth

auth = Blueprint('auth', __name__)


# Login
@auth.route('/auth/login', methods=['POST'])
def login():
    return AuthController().login()


# Change Password
@auth.route('/auth/change/password', methods=['PUT'])
@check_auth
def change_password():
    return AuthController().change_password()
