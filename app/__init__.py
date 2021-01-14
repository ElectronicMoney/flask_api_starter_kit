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
import click
from flask.cli import with_appcontext

import uuid
from werkzeug.security import generate_password_hash
from email_validator import validate_email, EmailNotValidError



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


# Create Super User Command
@app.cli.command()
@with_appcontext
@click.option(
    '--first_name', 
    required=True, 
    prompt=True, type=str, 
    help="The First Name of the user"
)

@click.option(
    '--last_name', 
    required=True, 
    prompt=True, 
    type=str,
    help="The Last Name of the user"
)
@click.option(
    '--username', 
    required=True, 
    prompt=True, 
    type=str,
    help="The Username of the user"
)
@click.option(
    '--email', 
    required=True, 
    prompt=True, 
    type=str,
    help="The Email of the user"
)
@click.option(
    '--password', 
    prompt=True, 
    required=True, 
    hide_input=True, 
    confirmation_prompt=True,
    help="The Password of the user"
)
def create_super_user(*args, **kwargs):
    """Create Super User."""
    from app.users.models.User import User
    from app.profiles.models.Profile import Profile

    user = User()
    profile = Profile()

    user.first_name = kwargs.get('first_name')
    user.last_name  = kwargs.get('last_name')
    user.username   = kwargs.get('username')
    user.email  = kwargs.get('email')     
    # Hash The Password
    user.password = generate_password_hash(
        kwargs.get('password'), 
        method='sha256'
    )
    user.user_public_id   = str(uuid.uuid4())
    user.is_admin   = True

    # Create Profile Here....
    profile.name  = "{} {}".format(user.first_name, user.last_name)
    profile.profile_public_id =  str(uuid.uuid4())
    profile.user  = user

    # # Add the user to the database
    db.session.add(user)
    # Then commit the session
    db.session.commit()

    click.echo('Super User Created Successfully!')


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