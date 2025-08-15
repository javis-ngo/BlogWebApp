from flask import request
from app.controller import controller
from app.dto.request.auth_request_dto import AuthRequestDto
from app.dto.request.signup_request_dto import SignupRequestDto
import app.services.auth_service as auth_service


@controller.route('/signup', methods=['POST'])
def signup():
    signup_request = request.get_json()
    signup_request_dto = SignupRequestDto(**signup_request)
    result = auth_service.sign_up(signup_request_dto.model_dump())
    return result, 201

@controller.route('/signin', methods=['POST'])
def signin():
    auth_request = request.get_json()
    auth_request_dto = AuthRequestDto(**auth_request)
    result = auth_service.sign_in(auth_request_dto.model_dump())
    return result, 200

@controller.route('/get-account', methods=['POST'])
def get_account():
    result = auth_service.get_account_info(request)
    return result, 200
