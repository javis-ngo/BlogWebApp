from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
import datetime

class Blog_Comments():
    __tablename__ = 'blog_comments'
    id = Column(Integer, primary_key=True)
    date_submitted = Column(DateTime, default=datetime.time())
    text = Column(String(500), nullable=False)
    blocked = Column(String(5), default="FALSE")
    if_blocked = Column(String(100), default="[removed]")
    post_id = Column(Integer, ForeignKey('blog_posts.id'))
    user_id = Column(Integer, ForeignKey('blog_user.id'))
    replied = Column(Boolean, nullable=True, default=False)
    reply_comment_id = Column(Integer, nullable=True, default=0)