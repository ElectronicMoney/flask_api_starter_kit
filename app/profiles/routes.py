from flask import Blueprint
from app.profiles.controllers.ProfileController import ProfileController

profiles = Blueprint('profiles', __name__)


# Get All profiles
@profiles.route('/profiles', methods=['GET'])
def get_profiles():
    return ProfileController().get_all_profiles()


# Get A Profile
@profiles.route('/profiles/<id>', methods=['GET'])
def get_user(id):
    return ProfileController().get_profile(id)