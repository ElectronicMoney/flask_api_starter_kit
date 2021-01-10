from sqlalchemy.exc import IntegrityError
from app import ma
from marshmallow import  INCLUDE


# User Schema
class AuthSchema(ma.Schema):

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

        # Fields to expose
        fields = (
            'username',
            'password',
            'token',
            )


auth_schema  = AuthSchema()
