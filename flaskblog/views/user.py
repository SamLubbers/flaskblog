from flask import Blueprint, render_template, request, redirect, url_for

from flaskblog.forms import SignUpForm, SignInForm

bp = Blueprint('user', __name__)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        # TODO call to register user function in services
        return redirect(url_for('index.index'))

    return render_template('user/signup.html', form=form)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm(request.form)
    if request.method == 'POST' and form.validate():
        # TODO call to login user function in services
        return redirect(url_for('index.index'))

    return render_template('user/signin.html', form=form)
