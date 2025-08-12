from pydantic import BaseModel

class AuthRequestDto(BaseModel):
    email: str
    password: str