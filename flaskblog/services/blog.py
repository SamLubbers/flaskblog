"""services module for interacting with the Blog model"""
from flaskblog.models import Blog, db
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()
five_minutes = 60 * 5 # default caching time is set to five minutes

def get_blog(blog_id):
    blog = cache.get(blog_id)
    if blog is None:
        print('blog is loaded from db')
        blog = Blog.query.filter_by(id=blog_id).one()
        cache.set(blog_id, blog, timeout=five_minutes)
    return blog

def insert_blog(blog_title, blog_text):
    if blog_title and blog_text:
        blog = Blog(title=blog_title, text=blog_text)
        db.session.add(blog)
        db.session.commit()
