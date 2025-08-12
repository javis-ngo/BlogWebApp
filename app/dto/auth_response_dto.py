from pydantic import BaseModel


class AuthResponseDto(BaseModel):
    idToken: str
    refreshToken: str