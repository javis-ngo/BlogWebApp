import datetime

from pydantic import BaseModel


class Post(BaseModel):
    post_id: str
    title: str
    body: str
    author: str
    category: str
    tags: list[str]

    def to_dynamodb_item(self):
        return {
            'PK': f'POST#{self.post_id}',
            'SK': 'METADATA',
            'data': {
                'title': self.title,
                'body': self.body
            },
            'category': self.category,
            'tags': self.tags,
            'date_posted': datetime.datetime,
            'author': self.author,
            'GSI1PK': f'CATEGORY#{self.category}',
            'GSI1SK': f'POST#{datetime.datetime}',
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