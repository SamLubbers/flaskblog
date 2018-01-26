from flask import render_template, request, redirect, url_for, flash
from flask.blueprints import Blueprint
from flaskblog import services
from flaskblog.forms import NewBlogForm
from flask_login import login_required

bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = NewBlogForm(request.form)
    if request.method == 'POST' and form.validate():
        services.insert_blog(blog_title=form.blog_title.data, blog_text=form.blog_text.data)
        flash(f'your blog "{form.blog_title.data}" was succesfully posted','success')
        return redirect(url_for('index.index'))
    return render_template('blog/new/new_blog.html', form=form)


@bp.route('/<int:blog_id>')
def view_blog(blog_id):
    blog = services.get_blog(blog_id)
    return render_template('blog/view/view_blog.html', blog=blog)
