import logging
import unittest
from datetime import datetime

from flask import current_app, g

from flaskblog import create_app
from tests.layouts import DefaultTestCase, RequestTestCase

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AppTestCase(DefaultTestCase):
    """tests that the app is set up properly"""

    def test_app(self):
        """app is loaded correctly"""
        with self.app.app_context():
            self.assertEqual(self.app, current_app)

    def test_config(self):
        """test that the correct configuration is loaded for tests"""

        self.assertTrue(self.app.testing)
        self.assertFalse(self.app.debug)


class RequestContextTestCase(RequestTestCase):

    def test_g_now(self):
        """we populate g.now with curret datetime for each request
        this tests g.now is available within a request context
        """
        with self.client:
            self.client.get('/')
            g_now = getattr(g, 'now', None)
            assert isinstance(g_now, datetime)

# class ViewsTestCase(unittest.TestCase):
#     """test that all routes return code 200 and render the correct template"""
#
#     def setUp(self):
#         self.app = create_app()
#         self.app.testing = True
#
#     def test_index(self):
#         with self.app.test_client() as client:
#             res = client.get('/')
#             assert res.status_code == 200
