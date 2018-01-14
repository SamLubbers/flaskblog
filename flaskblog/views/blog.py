from flask.blueprints import Blueprint
from flaskblog.models import db
from flaskblog.models import Blog
from flask import render_template, request, redirect, url_for

blog_bp = Blueprint('blog_bp', __name__, url_prefix='/blog')

@blog_bp.route('/new', methods=['GET', 'POST'])
def new_blog():
    if request.method == 'POST':
        blog_title = request.form.get('title')
        blog_text = request.form.get('text')
        if blog_title and blog_text: # make sure they are not null, later change this to the client side
            blog = Blog(title=blog_title,text=blog_text)
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for('index.blog_entries'))
    return render_template('blog/new_blog_entry.html')

@blog_bp.route('/<int:blog_id>')
def blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).one()
    return render_template('blog/blog_bp.html',blog=blog)