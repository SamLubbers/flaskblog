from flask import Blueprint, render_template, request, redirect, url_for, flash

from flaskblog.forms import SignUpForm, SignInForm
from flaskblog.services.user import create_user, signin_user
from flask_login import logout_user

bp = Blueprint('user', __name__)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        if create_user(form.username.data, form.password.data):
            flash('you have succesfully created a new account',
                  category='success')
            return redirect(url_for('index.index'))
        else:
            flash('username already exists', category='danger')
            return redirect(url_for('user.signup'))

    return render_template('user/signup.html', form=form)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm(request.form)
    if request.method == 'POST' and form.validate():
        if signin_user(form.username.data, form.password.data):
            flash('you have succesfully logged in',
                  category='success')
            return redirect(url_for('index.index'))
        else:
            flash('incorrect username and password combination', category='danger')
            return redirect(url_for('user.signin'))

    return render_template('user/signin.html', form=form)
