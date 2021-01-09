from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from app import db


# User Model
class User(db.Model):

    __tablename__ = 'user'

    id         = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name  = db.Column(db.String(100), nullable=False)
    username   = db.Column(db.String(80), unique=True, nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(80))
    is_admin   = db.Column(db.Boolean, default=False)
    is_active  = db.Column(db.Boolean, default=True)
    user_public_id  = db.Column(db.String(62), unique=True, nullable=False)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, default=datetime.utcnow)

    profile    = db.relationship('Profile', uselist=False, backref=db.backref('user', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username
