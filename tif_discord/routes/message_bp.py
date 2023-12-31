from flask import Blueprint
from ..controllers.message_controls import MessageController

message_bp = Blueprint('message_bp', __name__)

message_bp.route('/<int:id_channel>', methods=['GET'])(MessageController.get_all)
message_bp.route('/one/<int:id_message>', methods=['GET'])(MessageController.get_one)
message_bp.route('/', methods=['POST'])(MessageController.create_message)
message_bp.route('/', methods=['PUT'])(MessageController.update_message)
message_bp.route('/<int:id_message>', methods=['DELETE'])(MessageController.delete_message)