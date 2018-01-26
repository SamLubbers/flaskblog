from flask_login import LoginManager
from flaskblog.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()