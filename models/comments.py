import datetime

class Comment:
    def __init__(self, comment_id: str, user: str, post_id: int, text: str):
        self.comment_id = comment_id
        self.user = user
        self.post_id = post_id
        self.text = text

    def to_dynamodb_item(self):
        return {
            'PK': f'USER#{self.user}',
            'SK': f'COMMENT#{self.comment_id}',
            'post_id': self.post_id,
            'created_at': datetime.time(),
        }