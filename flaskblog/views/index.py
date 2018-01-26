from flask import render_template
from flask.blueprints import Blueprint

from flaskblog import services

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    blogs = services.get_all_blogs()
    return render_template('index/index.html', blogs=blogs)
