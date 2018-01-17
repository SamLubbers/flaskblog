from ._db import db

blog_tag = db.Table('blog_tag',
                    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id'), primary_key=True),
                    db.Column('tag_name', db.String(30), db.ForeignKey('tag.name'), primary_key=True),
                    )