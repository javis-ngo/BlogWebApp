import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime


class Blog_Bookmark():
    __tablename__ = 'blog_bookmark'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('blog_user.id'))
    post_id = Column(Integer, ForeignKey('blog_post.id'))
    date_submitted = Column(DateTime, default=datetime.time())

    def __repr__(self):
        return f"<Bookmark>"

class Bookmark:
    def __init__(self, user, post_id):
        self.user = user
        self.post_id = post_id

    def to_dynamodb_item(self):
        return {
            'PK': f'USER#{self.user}',
            'SK': f'BOOKMARK#{self.post_id}',
            'post_id': self.post_id,
            'created_at': datetime.time(),
        }