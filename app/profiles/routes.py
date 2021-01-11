from flask import Blueprint
from app.profiles.controllers.ProfileController import ProfileController
from app.auth.Auth import check_auth, auth

profiles = Blueprint('profiles', __name__)


# Get All profiles
@profiles.route('/profiles', methods=['GET'])
@check_auth
def get_profiles():
    return ProfileController().get_all_profiles()


# Get A Profile
@profiles.route('/profile', methods=['GET'])
@check_auth
def get_profile():
    return ProfileController().get_profile()