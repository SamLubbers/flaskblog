from datetime import datetime
from ._db import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    pubdate = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Blog(title='{self.title}')>"