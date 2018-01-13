import os

class Config(object):
    """Base config class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "not so secret base key"

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/flaskblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False