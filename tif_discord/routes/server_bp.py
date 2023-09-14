from flask import Blueprint
from ..controllers.server_controls import ServerController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/', methods=['GET'])(ServerController.get_all)
server_bp.route('/user', methods=['GET'])(ServerController.get_servers_user)
server_bp.route('/<int:id_server>', methods=['GET'])(ServerController.get_one)
server_bp.route('/', methods=['POST'])(ServerController.create_server)
server_bp.route('/<int:id_server>', methods=['PUT'])(ServerController.update_server)
server_bp.route('/<int:id_server>', methods=['DELETE'])(ServerController.delete_server)