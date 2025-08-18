from app.controller import controller
from flask import request
import app.services.user_service as user_service

@controller.route('/user', methods=['POST'])
def update_user():
    result = user_service.update_user(request)
    return result, 200