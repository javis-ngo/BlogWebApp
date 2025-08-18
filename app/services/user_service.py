from botocore.exceptions import ClientError

from app.dto.request.update_user_request import UpdateAccountRequestDTO
import app.repositories.user_repository as user_repository
from app.error_handlers.custom_api_error import CustomAPIError
from app.services import auth_service


def update_user(request):
    try:
        user_info = auth_service.validate_token(request)
        email = user_info['users'][0]['email']
        user = user_repository.get_user_by_email(email)
        if user:
            user.from_request_json(request.get_json(force=True))
            result = user_repository.update_user(user)
            return result["Attributes"]["data"]
        else:
            raise CustomAPIError("User not found", 400)
    except CustomAPIError as e:
        raise e
    except ClientError:
        raise CustomAPIError("Error with dynamoDb", 400)