import jwt
from flask import request, jsonify
from functools import wraps
from app.settings import ACCESS_TOKEN_SECRETE
from app.errors import http_error
from app.users.models.User import User

# Authentication Decorator
def check_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # get the token from the request headers
        access_token = request.headers.get('authorization')
        token = access_token.split(" ")[1]
        # return token
        # Check if we have token
        if not token:
            return http_error("Token Is missing on the request header!", 403)
        
        try:
            payload = jwt.decode(token, ACCESS_TOKEN_SECRETE, algorithms="HS256")
        except:
            return http_error("Invalid Token!", 403)
        return f(*args, **kwargs)

    # return the decorated function
    return decorated



# Authentication Decorator
def auth():
    # get the token from the request headers
    access_token = request.headers.get('authorization')
    token = access_token.split(" ")[1]
    # return token
    # Check if we have token
    if not token:
        return None
    try:
        payload = jwt.decode(token, ACCESS_TOKEN_SECRETE, algorithms="HS256")
        #Get The User public Id from the payload 
        user_public_id = payload.get('user')['user_public_id']
        # Try to get the user using the provided token
        user = User.query.filter_by(user_public_id=user_public_id).first()
    except:
        return None
    return {'user': user}

