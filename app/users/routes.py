from flask import Blueprint
from app.users.controllers.UserController import UserController
from app.auth.Auth import check_auth, auth

users = Blueprint('users', __name__)


# Create User
@users.route('/users', methods=['POST'])
def create_user():
    return UserController().create_user()


# Get All Users
@users.route('/users', methods=['GET'])
@check_auth
def get_users():
    return UserController().get_all_users()


# Get A User
@users.route('/users/<id>', methods=['GET'])
@check_auth
def get_user(id):
    return UserController().get_user(id)


# Update A User
@users.route('/users/<id>', methods=['PUT'])
@check_auth
def update_user(id):
    return UserController().update_user(id)

# Delete A User
@users.route('/users/<id>', methods=['DELETE'])
@check_auth
def delete_users(id):
    return UserController().delete_user(id)

# Promote A User
@users.route('/users/promote/<id>', methods=['PUT'])
@check_auth
def promote_user(id):
    return UserController().promote_user(id)