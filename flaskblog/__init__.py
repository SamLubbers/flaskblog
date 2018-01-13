from flask import Flask
from config import load_config

def create_app():
    app = Flask(__name__)

    # app configuration
    config = load_config()
    app.config.from_object(config)

    # register components
    register_db(app)

    return app

def register_db(app):
    """Register models"""
    from .models import db
    db.init_app(app=app)



# views
import flaskblog.views

# error handler views
import flaskblog.error_handlers

# template filters
import flaskblog.filters