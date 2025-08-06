from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship


class Blog_Themes():
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    theme = Column(String(80), nullable=False)
    picture = Column(String(80), nullable=False)
    picture_source = Column(Text, nullable=False)
    posts = relationship('Blog_Posts', backref='theme', lazy='dynamic')

    def __repr__(self):
        return f"<Theme: {self.id} {self.theme}>"