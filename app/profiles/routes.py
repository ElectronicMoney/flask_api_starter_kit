from flask import Blueprint
from app.profiles.controllers.ProfileController import ProfileController
from app.auth.Auth import auth

profiles = Blueprint('profiles', __name__)


# Get All profiles
@profiles.route('/profiles', methods=['GET'])
def get_profiles():
    return ProfileController().get_all_profiles()


# Get A Profile
@profiles.route('/profiles/<id>', methods=['GET'])
@auth
def get_profile(id):
    return ProfileController().get_profile(id)