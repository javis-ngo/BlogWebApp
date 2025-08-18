from pydantic import BaseModel


class UpdateAccountRequestDTO(BaseModel):
    username: str
    about: str
    avatar: str