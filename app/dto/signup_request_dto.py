from pydantic import BaseModel


class SignupRequestDto(BaseModel):
    username: str
    email: str
    password: str
    about: str
    avatar: str