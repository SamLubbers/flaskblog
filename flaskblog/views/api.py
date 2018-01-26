from flask import jsonify, abort, make_response
from flask.blueprints import Blueprint
from sqlalchemy.orm.exc import NoResultFound

from flaskblog.services import get_all_blogs, get_blog

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/allblogs')
def allblogs():
    all_blogs = [blog.serialize for blog in get_all_blogs()]
    if not all_blogs:
        abort(404)
    else:
        return jsonify(all_blogs=all_blogs)


@bp.route('/blog/<int:blog_id>')
def blog(blog_id):
    try:
        blog = get_blog(blog_id)
    except NoResultFound:
        return abort(404)
    return jsonify(blog=blog.serialize)


@bp.errorhandler(404)
def api_404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
