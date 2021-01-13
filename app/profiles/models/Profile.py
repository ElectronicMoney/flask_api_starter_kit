from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app import db
from datetime import datetime
from app.users.models.User import User


# User Model
class Profile(db.Model):
    __tablename__ = 'profile'


    profile_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profile_picture_url = db.Column(db.String(100), nullable=False, default="avatar.png")
    profile_public_id    = db.Column(db.String(62), unique=True, nullable=False)
    profile_created_at    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    profile_updated_at    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return '<Profile %r>' % self.username

