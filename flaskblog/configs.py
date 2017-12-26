from flaskblog import app
from os import path

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE = path.join(app.instance_path, 'flaskblog.db')

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY='development key'
    USERNAME='admin'
    PASSWORD='default'

class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY='testing key'
    USERNAME='admin'
    PASSWORD='default'
