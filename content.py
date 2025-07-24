from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    post_type = db.Column(db.String(50), default='post')  # post, page, event, news
    status = db.Column(db.String(20), default='published')  # draft, published
    featured_image = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    author = db.relationship('User', backref=db.backref('posts', lazy=True))
    categories = db.relationship('Category', secondary='post_category', back_populates='posts')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 關聯
    posts = db.relationship('Post', secondary='post_category', back_populates='categories')

# 多對多關聯表
post_category = db.Table('post_category',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    location = db.Column(db.String(255))
    registration_required = db.Column(db.Boolean, default=False)
    max_participants = db.Column(db.Integer)
    contact_info = db.Column(db.Text)
    featured_image = db.Column(db.String(255))
    status = db.Column(db.String(20), default='active')  # active, cancelled, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Magazine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    issue_number = db.Column(db.String(50), nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)
    cover_image = db.Column(db.String(255))
    pdf_file = db.Column(db.String(255))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

