from flask import  jsonify

# Error Message Handler
def http_error(message, code):
    # Check the status code
    if code == 200:
        status_type = 'Ok!' 

    elif code == 201:
        status_type = 'Created!' 
    
    elif code == 204:
        status_type = 'No Content!' 

    elif code == 400:
        status_type = 'Bad Request!' 

    elif code == 401:
        status_type = 'Unauthorized!' 

    elif code == 402:
        status_type = 'Payment Required!' 

    elif code == 403:
        status_type = 'Forbidden!' 

    elif code == 404:
        status_type = 'Not Found!' 

    elif code == 405:
        status_type = 'Method Not Allowed!' 
    
    elif code == 500:
        status_type = 'Internal Server Error!' 

    return jsonify({
            "error": {
                "type": status_type,
                "message": message,
                "code": code
            }
        }), code

