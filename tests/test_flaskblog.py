from flask import template_rendered, request, url_for, current_app, g
from contextlib import contextmanager
import flaskblog
import unittest
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@contextmanager
def captured_templates(app):
    """use signals to test the correct template is loaded"""
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


class AppContextTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True

    def test_current_app(self):
        with self.app.app_context():
            assert current_app == self.app


class RequestContextTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True

    def test_g_now(self):
        """we populate g.now with curret datetime for each request
        this tests g.now is available within a request context
        """
        with self.app.test_client() as client:
            client.get('/')
            g_now = getattr(g, 'now', None)
            assert isinstance(g_now, datetime)


class TempalatesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True
        self.test_client = self.app.test_client()

    def test_index_template(self):
        """test the right template is loaded"""
        with captured_templates(self.app) as templates:
            rv = self.test_client.get('/')
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'index/index.html'


class ViewsTestCase(unittest.TestCase):
    """test that all routes return code 200"""
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True

    def test_index(self):
        with self.app.test_client() as client:
            res = client.get('/')
            assert res.status_code == 200


class UrlforTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True

    def test_index(self):
        with self.app.test_request_context():
            assert url_for('index.index') == '/'
