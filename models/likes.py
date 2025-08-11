import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime


class Blog_Likes():
    __tablename__ = 'blog_likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('blog_user.id'))
    post_id = Column(Integer, ForeignKey('blog_post.id'))
    date_submitted = Column(DateTime, default=datetime.time())

    def __repr__(self):
        return f"<Like>"

class Like:
    def __init__(self, user, post_id):
        self.user_id = user
        self.post_id = post_id

    def to_dynamodb_item(self):
        return {
            'PK': f'POST#{self.post_id}',
            'SK': f'LIKE#{self.user_id}',
            'user_id': self.user_id,
            'created_at': datetime.time(),
        }