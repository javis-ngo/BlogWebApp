import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    about: str
    admin_notes: Optional[str] = ""
    avatar: str

    def to_dynamodb_item(self):
        return {
            'PK': f'USER#{self.email}',
            'SK': 'METADATA',
            'data': {
                'username': self.username,
                'email': self.email,
                'about': self.about,
                'admin_notes': self.admin_notes,
                'avatar': self.avatar,
            },
            'created_at': datetime.time().isoformat()
        }