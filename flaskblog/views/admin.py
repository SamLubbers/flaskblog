from flask.views import View
from flask import render_template, Blueprint
from flaskblog.models import Blog, Tag, User
from sqlalchemy.orm import joinedload
from sqlalchemy import inspect

bp = Blueprint('admin', __name__, url_prefix='/admin')


class ListView(View):
    """Pluggable view that renders a template that displays all data of a model in the database"""

    def __init__(self, model):
        self.model = model
        self.attributes = [att for att in self.model.__dict__.keys() if att[:1] != '_']

    def dispatch_request(self):
        data = self.model.query.options().all()
        model_name = self.model.__name__.lower()
        return render_template('admin/list.html', model=model_name, data=data, attributes=self.attributes)

bp.add_url_rule('/blog', view_func=ListView.as_view('blog_admin', model=Blog))
bp.add_url_rule('/user', view_func=ListView.as_view('user_admin', model=User))
bp.add_url_rule('/tag', view_func=ListView.as_view('tag_admin', model=Tag))