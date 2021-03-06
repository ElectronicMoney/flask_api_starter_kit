from sqlalchemy.exc import IntegrityError
from app import ma
from marshmallow import  INCLUDE


# User Schema
class UserSchema(ma.Schema):

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

        # Fields to expose
        fields = (
            'user_public_id',
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password',
            'is_admin',
            'is_active',
            'created_at',
            'updated_at'
            )


user_schema  = UserSchema()
users_schema = UserSchema(many=True)
