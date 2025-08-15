import datetime
import uuid

from pydantic import BaseModel


class Post(BaseModel):
    post_id: str = uuid.uuid4().hex
    title: str
    body: str
    images: list[str] = []
    author: str = ""
    category: str
    tags: list
    date_posted: int

    def to_dynamodb_item(self):
        return {
            'PK': f'POST#{self.post_id}',
            'SK': 'METADATA',
            'data': {
                'title': self.title,
                'body': self.body,
                'images': self.images,
            },
            'category': self.category,
            'tags': self.tags,
            'date_posted': self.date_posted,
            'author': self.author,
            'GSI1PK': f'CATEGORY#{self.category}',
            'GSI1SK': f'POST#{self.date_posted}',
            'GSI3PK': f'USER#{self.author}',
        }

    def to_tag_items(self):
        return [
            {
                'PK': f'POST#{self.post_id}',
                'SK': f'TAG#{tag}',
                'GSI2PK': f'TAG#{tag}',
                'GSI2SK': f'POST#{datetime.datetime}',
                'post_id': self.post_id
            }
            for tag in self.tags
        ]