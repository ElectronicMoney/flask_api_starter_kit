from app import ma

# User Schema
class UserSchema(ma.Schema):

    class Meta:
        # Fields to expose
        fields = (
            'user_id',
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password',
            'is_admin',
            'is_active',
            )