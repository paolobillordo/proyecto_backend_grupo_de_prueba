from flask import Flask
from config import Config
from .routes.user_bp import user_bp
from .routes.server_bp import server_bp


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp, url_prefix = '/users')
    app.register_blueprint(server_bp, url_prefix = '/servers')


    return app