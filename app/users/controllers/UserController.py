from flask import request, jsonify
from app.users.models.User import User
from app.users.schema import UserSchema
from app import db


class UserController():

    def __init__(self):
        # Init Schema
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)


    # Get All Users
    def get_all_users(self):
        all_users = User.query.all()
        all_users_result = self.users_schema.dump(all_users)
        return jsonify(all_users_result)
        

    # Get User
    def get_user(self, id):
        user = User.query.get(id)
        user_result = self.user_schema.dump(user)
        return jsonify(user_result)


    # Update User
    def update_user(self, id):
        name     = request.json['name']
        username = request.json['username']
        password = request.json['password']
        email    = request.json['email']

        # get the user you want tot udate
        user = User.query.get(id)

        user.name     = name
        user.username = username
        user.password = password
        user.email    = email

        db.session.commit()

        return self.user_schema.jsonify(user)

    # Delete User
    def delete_user(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return self.user_schema.jsonify(user)