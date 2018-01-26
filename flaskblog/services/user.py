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

def signin_user(username, password):
    # check that user does exist in db
    user = User.query.filter_by(username=username).first()
    if not user:
        return False
    # check that passwords match
    if user.password != password:
        return False
    # login user
    login_user(user)
    return True
