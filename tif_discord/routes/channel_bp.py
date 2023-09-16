from flask import Blueprint
from ..controllers.channel_controls import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/<name_server>', methods=['GET'])(ChannelController.get_all)
channel_bp.route('/<int:id_channel>', methods=['GET'])(ChannelController.get_one)
channel_bp.route('/', methods=['POST'])(ChannelController.create_channel)
channel_bp.route('/<int:id_channel>', methods=['PUT'])(ChannelController.update_channel)

