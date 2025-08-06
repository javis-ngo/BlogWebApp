from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

class Blog_Posts():
    __tablename__="blog_posts"
    id = Column(Integer, primary_key=True)
    date_posted = Column(DateTime, nullable=False, default= datetime.time())
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    picture = Column(String(255), nullable=True, default="")