from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='posts')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    published = Column(Boolean, default=False)