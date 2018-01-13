from flask import Flask
from config import load_config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app configuration
config = load_config()
app.config.from_object(config)

# database
db = SQLAlchemy(app)
import flaskblog.models

# views
import flaskblog.views

# error handler views
import flaskblog.error_handlers

# template filters
import flaskblog.filters