from flask.blueprints import Blueprint
from flask import request, render_template, session, redirect, url_for
from flaskblog.models import db
from flaskblog.models import Blog

user_bp = Blueprint('user_bp', __name__)

# @user_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form.get('username') != app.config['USERNAME']:
#             error = 'invalid username'
#         elif request.form.get('password') != app.config['PASSWORD']:
#             error = 'invalid password'
#         else:
#             session['logged_in'] = True
#             return redirect(url_for('blog_entries'))
#     return render_template('login.html', error=error)
#
# @user_bp.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     return redirect(url_for('blog_entries'))