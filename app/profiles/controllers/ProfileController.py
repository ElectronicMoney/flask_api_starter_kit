from flask import request, jsonify
from app import db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from app.errors import http_error
from email_validator import validate_email, EmailNotValidError
from app.profiles.schema import profile_schema, profiles_schema
from app.profiles.models.Profile import Profile


class ProfileController():

    def __init__(self):
        # Init Schema
        self.profile_schema = profile_schema
        self.profiles_schema = profiles_schema
        self.profile = Profile()


    # Get All Users
    def get_all_profiles(self):
        all_profiles = Profile.query.all()
        all_profiles_result = self.profiles_schema.dump(all_profiles)
        return jsonify(all_profiles_result)
        

    # Get Profile
    def get_profile(self, id):
        profile = Profile.query.filter_by(profile_public_id=id).first()
        # Check if not the profile
        if not profile:
            return http_error("No profile Found!", 404)

        profile_result = self.profile_schema.dump({
            "name": profile.name,
            "profile_avatar": profile.profile_avatar,
            "profile_created_at": profile.profile_created_at,
            "profile_public_id": profile.profile_public_id,
            "profile_updated_at": profile.profile_updated_at,
            "email": profile.user.email,
            "password": profile.user.password,
            "is_admin": profile.user.is_admin,
            "is_active": profile.user.is_active
        })

        return jsonify(profile_result)
