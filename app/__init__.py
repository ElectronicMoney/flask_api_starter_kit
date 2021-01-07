from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app.settings import SQLALCHEMY_TRACK_MODIFICATIONS

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


def create_app():
    from app.users import users

    # Register All The App Blueprints here
    app.register_blueprint(users)

    return app