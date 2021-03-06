import os
import jinja2
from config import load_config
from flask import Flask, render_template
from werkzeug.wsgi import SharedDataMiddleware

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # app configuration
    config = load_config()
    app.config.from_object(config)
    app.config.from_envvar('CONFIG', silent=True)  # override default config with production config in instance folder

    # Serve static files
    if app.debug or app.testing:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/pages': os.path.join(app.config.get('PROJECT_PATH'), 'flaskblog/pages')
        })

    # register components
    register_db(app)
    register_jinja(app)
    register_views(app)
    register_prerequest_handlers(app)
    register_error_handlers(app)
    register_login(app)

    return app


def register_db(app):
    """Register models"""
    from .models import db
    db.init_app(app=app)


def register_views(app):
    """Register views"""
    from . import views
    from flask import Blueprint

    for module in _import_submodules_from_package(views):
        bp = getattr(module, 'bp')
        if bp and isinstance(bp, Blueprint):
            app.register_blueprint(bp)


def register_jinja(app):
    """register jinja filters, templates..."""

    app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader([
            os.path.join(app.config.get('PROJECT_PATH'), 'flaskblog/macros'),
            os.path.join(app.config.get('PROJECT_PATH'), 'flaskblog/pages')
        ])
    ])

    # registering filters to templates
    @app.context_processor
    def filters():
        from .utils import filters
        return dict(trim=filters.trim,
                    format_date=filters.format_date,
                    getattr=getattr)


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


def register_prerequest_handlers(app):
    from .utils.prerequests import set_now
    app.before_request(set_now)


def register_login(app):
    from flaskblog.utils.login import login_manager
    login_manager.init_app(app)

def _import_submodules_from_package(package):
    from pkgutil import iter_modules
    from importlib import import_module
    modules = []

    for importer, modname, ispkg in iter_modules(package.__path__,
                                                 prefix=package.__name__ + "."):
        modules.append(import_module(modname))

    return modules
