from flask.blueprints import Blueprint
from flaskblog.models import db
from flaskblog.models import Blog
from flask import render_template, request, redirect, url_for

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/new', methods=['GET', 'POST'])
def new_blog():
    if request.method == 'POST':
        blog_title = request.form.get('title')
        blog_text = request.form.get('text')
        if blog_title and blog_text: # make sure they are not null, later change this to the client side
            blog = Blog(title=blog_title,text=blog_text)
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for('index.index'))
    return render_template('blog/new_blog.html')

@bp.route('/<int:blog_id>')
def view_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).one()
    return render_template('blog/view_blog.html',blog=blog)