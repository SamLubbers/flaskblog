from datetime import datetime
from ._db import db
from ._relationship_tables import blog_tag
from flaskblog.utils.serializing import dump_datetime


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    pubdate = db.Column(db.DateTime, default=datetime.utcnow())

    tags = db.relationship('Tag', secondary=blog_tag, back_populates='blogs')

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='blogs')

    def __repr__(self):
        return f"Blog({self.title})"

    def author_name(self):
        print('PROPERTY CALLED')
        if self.author is None:
            return None
        return self.author.name

    def tag_names(self):
        tags = [tag.name for tag in self.tags if tag]
        if not tags:
            return None
        return tags

    @property
    def serialize(self):
        """Return object data in a format easily serializable to json"""
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'pubdate': dump_datetime(self.pubdate),
            'tags': self.tag_names(),
            'author': self.author_name()
        }


class Tag(db.Model):
    name = db.Column(db.String(30), primary_key=True)
    blogs = db.relationship('Blog', secondary=blog_tag, back_populates='tags')

    def __repr__(self):
        return f"Tag({self.name})"
