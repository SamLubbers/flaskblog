from ._db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80))

    blogs = db.relationship('Blog', back_populates='author', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"User({self.username})"
