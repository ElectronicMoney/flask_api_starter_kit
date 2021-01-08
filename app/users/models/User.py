from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app import db


# User Model
class User(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name  = db.Column(db.String(100), nullable=False)
    username   = db.Column(db.String(80), unique=True, nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(80))
    is_admin   = db.Column(db.Boolean)
    is_active  = db.Column(db.Boolean)
    user_id    = db.Column(db.String(62), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

