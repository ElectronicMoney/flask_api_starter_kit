from flask import Flask, abort, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app.settings import SQLALCHEMY_TRACK_MODIFICATIONS
from werkzeug.exceptions import HTTPException, default_exceptions
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from app.settings import UPLOAD_FOLDER
from app.middlewares.AuthMiddleware import AuthMiddleware


# Init App
app = Flask(__name__)

# Connect Middlewares with the app
app.wsgi_app = AuthMiddleware(app.wsgi_app)

# Upload Allowed File Extentions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# Upload Config File
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


base_dir = os.path.abspath(os.path.dirname(__file__))



# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Migration Manager
migrate = Migrate(app, db)

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

    # Import All Modules Here....
    from app.users import users
    from app.profiles import profiles
    from app.auth import auth

    # Register All The App Blueprints here
    app.register_blueprint(users)
    app.register_blueprint(profiles)
    app.register_blueprint(auth)

    # Create The Database and all tables
    # db.create_all()
    # Application-factory pattern
    db.init_app(app)
    migrate.init_app(app, db)

    # Convert  All HTML Exceptions to Json Format
    for ex in default_exceptions:
        app.register_error_handler(ex, error_handler)

    return app