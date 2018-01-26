"""services module for interacting with the Blog model"""
from flaskblog.models import Blog, db, User
from flaskblog.utils.api import make_public_blog
from werkzeug.contrib.cache import SimpleCache
from flask import current_app

cache = SimpleCache()


def get_blog(blog_id):
    blog = cache.get(blog_id)
    if blog is None:
        blog = Blog.query.filter_by(id=blog_id).one()
        cache.set(blog_id, blog, timeout=current_app.config['CACHE_TIMEOUT'])
    return blog


def insert_blog(blog_title, blog_text, username):
    blog = Blog(title=blog_title, text=blog_text)
    blog.author = User.query.filter_by(username=username).first()
    db.session.add(blog)
    db.session.commit()


def get_all_blogs():
    return Blog.query.order_by(Blog.pubdate.desc()).all()

def get_all_blogs_with_uri():
    """all blogs data + blog URI"""
    blogs = [blog.serialize for blog in get_all_blogs()]
    blogs = [make_public_blog(blog) for blog in blogs]
    return blogs
