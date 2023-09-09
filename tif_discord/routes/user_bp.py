from flask import Blueprint
from ..controllers.user_controls import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(UserController.get_all)
user_bp.route('/<int:id_user>', methods=['GET'])(UserController.get_one)
user_bp.route('/', methods=['POST'])(UserController.create_user)
user_bp.route('/<int:id_user>', methods=['PUT'])(UserController.update_user)
user_bp.route('/<int:id_user>', methods=['DELETE'])(UserController.delete_user)