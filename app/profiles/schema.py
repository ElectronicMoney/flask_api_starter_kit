from sqlalchemy.exc import IntegrityError
from app import ma
from marshmallow import  INCLUDE


# User Schema
class ProfileSchema(ma.Schema):

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

        # Fields to expose
        fields = (
            'profile_public_id',
            'name', 
            'email', 
            'password',
            'is_admin',
            'is_active',
            'profile_created_at',
            'profile_updated_at',
            'profile_avatar'
            )


profile_schema  = ProfileSchema()
profiles_schema = ProfileSchema(many=True)