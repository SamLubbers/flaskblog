from flask import render_template, request, redirect, url_for, flash
from flask.blueprints import Blueprint
from flaskblog import services

bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/new', methods=['GET', 'POST'])
def new_blog():
    if request.method == 'POST':
        blog_title = request.form.get('title')
        services.insert_blog(blog_title=blog_title,
                             blog_text=request.form.get('text'))
        flash(f'your blog "{blog_title}" was succesfully posted','success')
        return redirect(url_for('index.index'))
    return render_template('blog/new/new_blog.html')


@bp.route('/<int:blog_id>')
def view_blog(blog_id):
    blog = services.get_blog(blog_id)
    return render_template('blog/view/view_blog.html', blog=blog)
