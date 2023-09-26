from flask import Blueprint
from ..models.errores_y_excepciones import DatoInvalido

error = Blueprint("error", __name__)

@error.app_errorhandler(DatoInvalido)
def handle_bad_request(error):
    return error.get_response()