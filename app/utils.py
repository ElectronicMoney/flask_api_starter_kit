from marshmallow import ValidationError

# Custom validator
def validate_first_name(data):
    if not data:
        raise ValidationError("The First Name is Required!")