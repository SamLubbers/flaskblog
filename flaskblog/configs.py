from flaskblog import app
from os import path

class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY='development key'
    USERNAME='admin'
    PASSWORD='default'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flaskblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY='testing key'
    USERNAME='admin'
    PASSWORD='default'