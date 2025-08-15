from pydantic import BaseModel


class AuthResponseDto(BaseModel):
    pass
    idToken: str
    refreshToken: str