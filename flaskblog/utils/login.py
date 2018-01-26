from flask_login import LoginManager, login_user
from flaskblog.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()