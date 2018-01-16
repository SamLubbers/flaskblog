""""""
from flask import template_rendered, request
from contextlib import contextmanager
import flaskblog
import unittest
from blinker import signal

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


class TempalatesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True
        self.test_client = self.app.test_client()

    def test_index_template(self): # text the right is loaded
        with captured_templates(self.app) as templates:
            rv = self.test_client.get('/')
            assert rv.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'index/index.html'

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.create_app()
        self.app.testing = True
        self.test_client = self.app.test_client()

    def test_index_route(self):
        with self.app.test_request_context('/'):
            assert request.path == '/'


if __name__ == '__main__':
    unittest.main()

