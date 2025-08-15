from flask import Blueprint

error_handler = Blueprint('error_handler', __name__)

from app.error_handlers.custom_exception import register_error_handlers