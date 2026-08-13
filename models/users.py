from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from ..core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='author')