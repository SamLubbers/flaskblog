from ._db import db
from .blog import Blog

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    blogs = db.relationship('Blog', back_populates='author', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"<User(name='{self.name}')>"