from pydantic import BaseModel, EmailStr, constr


class SignupRequestDto(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=6)
    about: str
    avatar: str