import os
import pyrebase
from pydantic import ValidationError

from app.dto.auth_response_dto import AuthResponseDto
from app.error_handlers.custom_api_error import CustomAPIError
from app.models.user import User
from app.repositories import user_repository

firebaseConfig = {
  'apiKey': os.getenv("FIREBASE_API_KEY"),
  'authDomain': os.getenv("FIREBASE_AUTH_DOMAIN"),
  'projectId': os.getenv("FIREBASE_PROJECT_ID"),
  'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET"),
  'messagingSenderId': os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
  'appId': os.getenv("FIREBASE_APP_ID"),
  'measurementId': os.getenv("FIREBASE_MEASUREMENT_ID"),
  'databaseURL': os.getenv("FIREBASE_DATABASE_URL")
}

def sign_up(signup_request_dto):
    global result
    try:
        user = User(**signup_request_dto)
        firebase = pyrebase.initialize_app(firebaseConfig)
        auth = firebase.auth()
        user_repository.create_user(user)
        user_response = auth.create_user_with_email_and_password(signup_request_dto["email"],
                                                                 signup_request_dto["password"])
        result = AuthResponseDto(**user_response)
    except ValidationError as e:
        raise CustomAPIError(e, 400)
    except Exception as e:
        raise CustomAPIError(e, 500)
    return result.model_dump()
