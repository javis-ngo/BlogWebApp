import datetime

from pydantic import BaseModel


class Like(BaseModel):
    user: str
    post_id: str

    def to_dynamodb_item(self):
        return {
            'PK': f'POST#{self.post_id}',
            'SK': f'LIKE#{self.user}',
            'user': self.user,
            'created_at': datetime.time(),
        }