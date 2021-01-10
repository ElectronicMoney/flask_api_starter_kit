from flask import Blueprint
from app.auth.controllers.AuthController import AuthController

auth = Blueprint('auth', __name__)


# Login
@auth.route('/login', methods=['POST'])
def login():
    return AuthController().login()
