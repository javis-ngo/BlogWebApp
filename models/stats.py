from sqlalchemy import Column, Integer


class Blog_Stats():
    __tablename__ = 'blog_stats'
    id = Column(Integer, primary_key=True)
    user_total = Column(Integer, nullable=False)
    user_active_total = Column(Integer, nullable=False)
    posts_approved = Column(Integer, nullable=False)
    comments_total = Column(Integer, nullable=False)
    likes_total = Column(Integer, nullable=False)
    bookmarks_total = Column(Integer, nullable=False)

    def __repr__(self):
        return '<User Total: {}>'.format(self.user_total)