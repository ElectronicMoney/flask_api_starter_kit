from app import ma

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'username', 'email')