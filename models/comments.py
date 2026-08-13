from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from ..core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='comments')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    