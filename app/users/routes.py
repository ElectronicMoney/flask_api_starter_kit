from flask import Blueprint
from app.users.controllers.UserController import UserController

users = Blueprint('users', __name__)


# Create User
@users.route('/users', methods=['POST'])
def create_user():
    return UserController().create_user()


# Get All Users
@users.route('/users', methods=['GET'])
def get_users():
    return UserController().get_all_users()


# Get A User
@users.route('/users/<id>', methods=['GET'])
def get_user(id):
    return UserController().get_user(id)


# Update A User
@users.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return UserController().update_user(id)

# Delete A User
@users.route('/users/<id>', methods=['DELETE'])
def delete_users(id):
    return UserController().delete_user(id)