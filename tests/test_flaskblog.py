import logging
from datetime import datetime

from flask import current_app, g

from tests.layouts import DefaultTestCase, RequestTestCase
from tests.helpers import client_get_request

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

class ViewsTestCase(RequestTestCase):
    """test that all routes return code 200 and render the correct template"""

    @client_get_request('/')
    def test_index(self, response, template, context):
        self.success(response.status_code)
        self.assertEquals(template, 'index/index.html')