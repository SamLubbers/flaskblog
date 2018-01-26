from flaskblog.models import db, User
from flask_login import login_user


def create_user(username, password):
    # check that user does not exist in db
    if User.query.filter_by(username=username).first():
        return False
    # create user
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return True
