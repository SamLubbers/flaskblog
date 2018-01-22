from flask import jsonify
from flask.blueprints import Blueprint
from flaskblog.services import get_all_blogs

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/allblogs')
def allblogs():
    return jsonify(all_blogs=[blog.serialize for blog in get_all_blogs()])
