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
            'username',
            'is_admin',
            'is_active',
            'profile_created_at',
            'profile_updated_at',
            'profile_picture_url'
            )


profile_schema  = ProfileSchema()
profiles_schema = ProfileSchema(many=True)
