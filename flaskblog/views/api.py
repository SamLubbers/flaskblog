from flask import jsonify, abort
from flask.blueprints import Blueprint
from flaskblog.services import get_all_blogs, get_blog
from sqlalchemy.orm.exc import NoResultFound

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/allblogs')
def allblogs():
    # TODO exception handling if no blogs exist
    return jsonify(all_blogs=[blog.serialize for blog in get_all_blogs()])


@bp.route('/blog/<int:blog_id>')
def blog(blog_id):
    try:
        blog = get_blog(blog_id)
    except NoResultFound:
        # TODO return 404 without html
        return abort(404)
    return jsonify(blog=blog.serialize)
