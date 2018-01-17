from flask.views import View
from flask import render_template, Blueprint
from flaskblog.models import Blog, Tag, User

bp = Blueprint('admin', __name__, url_prefix='/admin')


class ListView(View):
    """Pluggable view that renders a template that displays all data of a model in the database"""

    def __init__(self, model):
        self.model = model

    def dispatch_request(self):
        data = self.model.query.all()
        return render_template('admin/list.html', model=self.model.__name__, data=data)

bp.add_url_rule('/blog', view_func=ListView.as_view('blog_admin', model=Blog))
bp.add_url_rule('/user', view_func=ListView.as_view('user_admin', model=User))
bp.add_url_rule('/tag', view_func=ListView.as_view('tag_admin', model=Tag))