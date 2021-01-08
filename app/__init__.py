from flask import Flask, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app.settings import SQLALCHEMY_TRACK_MODIFICATIONS
from werkzeug.exceptions import HTTPException, default_exceptions


# Init App
app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init Mashmallow
ma = Marshmallow(app)


# Handle All HTTPException
@app.errorhandler(Exception)
def error_handler(e):
    code = 500
    status_type = 'Internal Server Error!' 

    if isinstance(e, HTTPException):
        code = e.code
    # return the error message
    return jsonify({
            "error": {
                "type": status_type,
                "message": str(e),
                "code": code
            }
        }), code


def create_app():

    from app.users import users

    # Register All The App Blueprints here
    app.register_blueprint(users)

    # Create The Database and all tables
    db.create_all()

    # Convert  All HTML Exceptions to Json Format
    for ex in default_exceptions:
        app.register_error_handler(ex, error_handler)

    return app