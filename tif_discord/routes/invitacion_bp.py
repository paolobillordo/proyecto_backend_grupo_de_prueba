from flask import Blueprint
from ..controllers.invitacion_controls import InvitacionController

invitacion_bp = Blueprint('invitacion_bp', __name__)


invitacion_bp.route('/', methods=['POST'])(InvitacionController.enviar_invitacion)