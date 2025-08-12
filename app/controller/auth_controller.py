from flask import request
from app.controller import controller
from app.dto.signup_request_dto import SignupRequestDto
import app.services.auth_service as auth_service
from app.error_handlers.custom_api_error import CustomAPIError


@controller.route('/signup', methods=['POST'])
def signup():
  try:
      auth_request = request.get_json()
      signup_request_dto = SignupRequestDto(**auth_request)
      result = auth_service.sign_up(signup_request_dto.model_dump())
      return result, 201
  except CustomAPIError as e:
      raise e
