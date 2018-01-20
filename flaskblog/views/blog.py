from flask import render_template, request, redirect, url_for
from flask.blueprints import Blueprint
from flaskblog import services

bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/new', methods=['GET', 'POST'])
def new_blog():
    if request.method == 'POST':
        services.insert_blog(blog_title=request.form.get('title'),
                             blog_text=request.form.get('text'))
        return redirect(url_for('index.index'))
    return render_template('blog/new/new_blog.html')


@bp.route('/<int:blog_id>')
def view_blog(blog_id):
    blog = services.get_blog(blog_id)
    return render_template('blog/view/view_blog.html', blog=blog)
