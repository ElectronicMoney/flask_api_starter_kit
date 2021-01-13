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

# Upload Profile Picture
@profiles.route('/profile/picture/upload', methods=['POST'])
@check_auth
def upload_profile_picture():
    return ProfileController().upload_profile_picture()

# Get A  Profile Picture
@profiles.route('/profile/picture/<filename>', methods=['GET'])
@check_auth
def get_profile_picture(filename):
    return ProfileController().get_profile_picture(filename)