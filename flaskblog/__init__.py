from flask import Flask, render_template
from config import load_config
import os
import jinja2

def create_app():
    app = Flask(__name__)

    # app configuration
    config = load_config()
    app.config.from_object(config)

    # register components
    register_db(app)
    register_filters(app)
    register_views(app)
    register_error_handlers(app)

    return app

def register_db(app):
    """Register models"""
    from .models import db
    db.init_app(app=app)

def register_views(app):
    """Register vies"""
    from .views import index, blog_bp, user_bp
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(index)

def register_filters(app):
    """register jinja filters"""

    app.jinja_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader([
                os.path.join(app.config.get('PROJECT_PATH'), 'flaskblog/macros'),
                os.path.join(app.config.get('PROJECT_PATH'), 'flaskblog/pages')
            ])
        ])

    from .utils import filters
    app.jinja_env.filters['trim'] = filters.trim
    app.jinja_env.filters['format_date'] = filters.format_date


def register_error_handlers(app):
    """error handling"""
    error_tempalte = 'error/error.html'

    server_error_code = 500
    @app.errorhandler(server_error_code)
    def server_error(error):
        return render_template(error_tempalte, code=server_error_code), server_error_code

    gone_code = 410

    @app.errorhandler(gone_code)
    def gone(error):
        return render_template(error_tempalte, code=gone_code), gone_code

    not_found_code = 404

    @app.errorhandler(not_found_code)
    def not_found(error):
        return render_template(error_tempalte, code=not_found_code), not_found_code

    forbidden_code = 403

    @app.errorhandler(forbidden_code)
    def forbidden(error):
        return render_template(error_tempalte, code=forbidden_code), forbidden_code
