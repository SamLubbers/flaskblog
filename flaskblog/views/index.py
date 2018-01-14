from flask.blueprints import Blueprint
from flaskblog.models import Blog
from flask import render_template

index = Blueprint('index', __name__)

@index.route('/')
def blog_entries():
    entries = Blog.query.order_by(Blog.id).all()

    return render_template('blog/blog_entries.html', entries=entries)