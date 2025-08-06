from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

import datetime

from flask_login import UserMixin

class Blog_User(UserMixin):
    __tablename__ = 'blog_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.time())
    updated_at = Column(DateTime, nullable=False, default=datetime.time())
    about = Column(String(255), nullable=True, default="")
    picture = Column(String(255), nullable=True, default="")
    type = Column(String(255), nullable=True, default="")
    admin_notes = Column(Text, nullable=True, default="")
    posts = relationship('Blog_Post', backref='user', lazy=True)
    comments = relationship('Blog_Comment', backref='user', lazy=True)
    replies = relationship('Blog_Reply', backref='user', lazy=True)
    likes = relationship('Blog_Like', backref='user', lazy=True)
    bookmarks = relationship('Blog_Bookmark', backref='user', lazy=True)

    def __repr__(self):
        return f"<User: {self.id} {self.name} {self.email}>"
