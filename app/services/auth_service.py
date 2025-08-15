from gcloud.exceptions import ClientError
from pydantic import ValidationError

from app.dto.response.auth_response_dto import AuthResponseDto
from app.error_handlers.custom_api_error import CustomAPIError
from app.models.user import User
from app.repositories import user_repository
from app.services import auth
from app.utils.my_util import hash_password


def sign_up(signup_request_dto):
    global result
    try:
        if user_repository.get_user_by_email(signup_request_dto["email"]):
            raise CustomAPIError("Email already registered", 400)
        user = User(**signup_request_dto)
        hashed_password = hash_password(signup_request_dto["password"])
        user_repository.create_user(user)
        user_response = auth.create_user_with_email_and_password(signup_request_dto["email"], hashed_password)
        result = AuthResponseDto(**user_response)
    except ValidationError as e:
        raise CustomAPIError(e, 400)
    except ClientError as e:
        raise CustomAPIError("Client Error", 400)
    except CustomAPIError as e:
        raise CustomAPIError(e.message, e.status_code)
    except Exception as e:
        raise CustomAPIError(e, 500)
    return result.model_dump()

def sign_in(auth_request_dto):
    try:
        if user_repository.get_user_by_email(auth_request_dto["email"]):
            hashed_password = hash_password(auth_request_dto["password"])
            user_response = auth.sign_in_with_email_and_password(auth_request_dto["email"], hashed_password)
            return AuthResponseDto(**user_response).model_dump()
        else:
            raise CustomAPIError("User not found", 400)
    except CustomAPIError as e:
        raise CustomAPIError(e, e.status_code)
    except Exception as e:
        raise CustomAPIError(e, 500)

def get_account_info(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise CustomAPIError("No authorization header", 400)

    if not auth_header.startswith('Bearer '):
        raise CustomAPIError("Invalid Authorization header", 401)

    id_token = auth_header[7:]

    try:
        user_info = auth.get_account_info(id_token)
        return user_info
    except auth.InvalidIdTokenError:
        raise CustomAPIError("Invalid ID Token", 401)
    except auth.ExpiredIdTokenError:
        raise CustomAPIError("Expired ID Token", 401)
    except auth.AuthError as e:
        raise CustomAPIError(e.message, e.status_code)
    except Exception as e:
        raise CustomAPIError(e, 500)