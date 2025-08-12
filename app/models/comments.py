import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    comment_id: str
    user: str
    post_id: int
    text: str

    def to_dynamodb_item(self):
        return {
            'PK': f'USER#{self.user}',
            'SK': f'COMMENT#{self.comment_id}',
            'post_id': self.post_id,
            'created_at': datetime.time(),
        }