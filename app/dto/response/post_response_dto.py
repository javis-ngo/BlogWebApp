from pydantic import BaseModel


class PostResponseDto(BaseModel):
    title: str
    body: str
    images: list[str] = []
    author: str = ""
    category: str
    tags: list
    date_posted: int