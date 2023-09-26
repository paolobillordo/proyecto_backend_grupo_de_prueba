from flask import Flask
from config import Config
from flask_cors import CORS
from .routes.user_bp import user_bp
from .routes.server_bp import server_bp
from .routes.channel_bp import channel_bp
from .routes.message_bp import message_bp
from .routes.manejador_error import error

def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)
    app.secret_key = Config.SECRET_KEY

    app.register_blueprint(user_bp, url_prefix = '/users')
    app.register_blueprint(server_bp, url_prefix = '/servers')
    app.register_blueprint(channel_bp, url_prefix = '/channels')
    app.register_blueprint(message_bp, url_prefix = '/messages')

    app.register_blueprint(error)


    return app