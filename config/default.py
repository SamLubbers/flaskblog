import os

class Config(object):
    """Base config class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "not so secret base key"

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/flaskblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # caching
    CACHE_TIMEOUT = 60 * 5 # default caching timeout of ten minutes
