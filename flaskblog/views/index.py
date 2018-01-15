from flask.blueprints import Blueprint
from flaskblog.models import Blog
from flask import render_template

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    entries = Blog.query.order_by(Blog.id).all()

    return render_template('index/index.html', entries=entries)
