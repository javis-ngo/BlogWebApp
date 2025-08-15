from typing import Required

from pydantic import BaseModel, EmailStr, constr


class AuthRequestDto(BaseModel):
    email: EmailStr
    password: constr(min_length=6)