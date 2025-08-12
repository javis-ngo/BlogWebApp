import datetime

from pydantic import BaseModel

class Bookmark(BaseModel):
    user: str
    post_id: str

    def to_dynamodb_item(self):
        return {
            'PK': f'USER#{self.user}',
            'SK': f'BOOKMARK#{self.post_id}',
            'post_id': self.post_id,
            'created_at': datetime.time(),
        }