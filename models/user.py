import datetime

class User:
    def __init__(self, username: str, email: str, about: str, status: bool, admin_notes: str = "",
                 avatar: str = ""):
        self.username = username
        self.email = email
        self.about = about
        self.status = status
        self.admin_notes = admin_notes
        self.avatar = avatar

    def to_dynamodb_item(self):
        return {
            'PK': f'USER#{self.email}',
            'SK': 'METADATA',
            'data': {
                'username': self.username,
                'email': self.email,
                'about': self.about,
                'status': self.status,
                'admin_notes': self.admin_notes,
                'avatar': self.avatar,
            },
            'created_at': datetime.time().isoformat()
        }