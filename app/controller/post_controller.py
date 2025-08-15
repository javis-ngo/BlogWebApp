from app.controller import controller
from flask import request
import app.services.post_service as post_service

@controller.route('/post', methods=['POST'])
def create_post():
    return post_service.create_post(request), 200