from datetime import datetime
from ._db import db
from ._relationship_tables import blog_tag

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    pubdate = db.Column(db.DateTime, default=datetime.utcnow())

    tags = db.relationship('Tag', secondary=blog_tag, back_populates='blogs')

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='blogs')
    def __repr__(self):
        return f"<Blog(title='{self.title}')>"

class Tag(db.Model):
    name = db.Column(db.String(30), primary_key=True)
    blogs = db.relationship('Blog', secondary=blog_tag, back_populates='tags')

    def __repr__(self):
        return f"<Tag(name='{self.name}')>"
