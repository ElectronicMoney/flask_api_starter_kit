import jwt
from flask import request, jsonify
from functools import wraps
from app.settings import ACCESS_TOKEN_SECRETE
from app.errors import http_error

# Authentication Decorator
def auth(f):
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