from flask import Blueprint
from ..controllers.user_controls import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(UserController.get_all)
user_bp.route('/<int:id_user>', methods=['GET'])(UserController.get_one)
user_bp.route('/', methods=['POST'])(UserController.create_user)
user_bp.route('/', methods=['PUT'])(UserController.update_user)
user_bp.route('/<int:id_user>', methods=['DELETE'])(UserController.delete_user)
user_bp.route('/login', methods=['POST'])(UserController.login)
user_bp.route('/profile', methods=['GET'])(UserController.show_profile)
user_bp.route('/logout', methods=['GET'])(UserController.logout)
user_bp.route('/get_session',methods=['GET'])(UserController.get_session)