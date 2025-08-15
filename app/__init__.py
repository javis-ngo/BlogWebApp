from flask import Flask

from app.controller import controller
from app.error_handlers import register_error_handlers


def create_app():
    app = Flask(__name__)
    app.register_blueprint(controller)

    register_error_handlers(app)

    return app