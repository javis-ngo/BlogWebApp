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