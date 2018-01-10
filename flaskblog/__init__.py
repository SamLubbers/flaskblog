from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# app configuration
app.config.from_object('flaskblog.configs.DevelopmentConfig') # default config
app.config.from_pyfile('config.py', silent=True) # override default config with file in instance folder
app.config.from_envvar('CONFIG', silent=True) # override default config with file in envvar CONFIG

# database
import flaskblog.db_manager

# views
import flaskblog.views

# error handler views
import flaskblog.error_handlers