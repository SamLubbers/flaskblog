from flaskblog.models import Blog
from werkzeug.contrib.cache import SimpleCache

c = SimpleCache()
five_minutes = 60 * 5 # default caching time is set to five minutes

def get_blog(blog_id):
    blog = c.get(blog_id)
    if blog is None:
        print('blog is loaded from db')
        blog = Blog.query.filter_by(id=blog_id).one()
        c.set(blog_id, blog, timeout=five_minutes)
    return blog
