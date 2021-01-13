from marshmallow import ValidationError

# Custom validator
def validate_first_name(data):
    if not data:
        raise ValidationError("The First Name is Required!")


# Allow upload file extentions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS