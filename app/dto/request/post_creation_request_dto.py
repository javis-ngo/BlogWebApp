
from pydantic import BaseModel, Field


class PostCreateRequestDTO(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    body: str = Field(min_length=10)
    category: str = Field(min_length=2, max_length=50)
    tags: list = []
    date_posted: int