from flask import Flask, render_template
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

def register_views(app):
    """Register vies"""
    from .views import blog_bp, user_bp
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)

def register_error_handlers(app):
    """error handling"""
    server_error_code = 500

    @app.errorhandler(server_error_code)
    def server_error(error):
        return render_template('error.html', code=server_error_code), server_error_code

    gone_code = 410

    @app.errorhandler(gone_code)
    def gone(error):
        return render_template('error.html', code=gone_code), gone_code

    not_found_code = 404

    @app.errorhandler(not_found_code)
    def not_found(error):
        return render_template('error.html', code=not_found_code), not_found_code

    forbidden_code = 403

    @app.errorhandler(forbidden_code)
    def forbidden(error):
        return render_template('error.html', code=forbidden_code), forbidden_code


# views
import flaskblog.views

# error handler views
import flaskblog.error_handlers

# template filters
import flaskblog.filters