from flask import Blueprint

controller = Blueprint('controller', __name__)

from app.controller import auth_controller