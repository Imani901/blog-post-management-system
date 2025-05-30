# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    posts = relationship("Post", back_populates="category", cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    category = relationship("Category", back_populates="posts")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    commenter_name = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship("Post", back_populates="comments")
