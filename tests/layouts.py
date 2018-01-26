import os
import unittest

from flaskblog import create_app
from flaskblog.models import db


class DefaultTestCase(unittest.TestCase):
    """TestCase with setUP and TearDown code that all tests have in common

    All other test cases for flaskblog must subclass this class
    """

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        # app
        os.environ['APP_CONFIG_FILE'] = 'config.test'
        self.app = create_app()

        # db
        self.app.app_context().push()  # bind db to this app instance
        db.create_all()  # create tables in test db

    def tearDown(self):
        db.session.remove()  # ensure session is properly removed and that a new session is started with each test run
        db.drop_all()  # drop all tables in tests database so db is empty for next test case

    ##############################
    #### setup helper methods ####
    ##############################

class RequestTestCase(DefaultTestCase):
    """test case for making client requests to our application"""

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        super().setUp()  # load DefaultTestCase settings
        self.client = self.app.test_client()  #  create test client that can be used to make requests

    #############################
    #### test helper methods ####
    #############################

    def success(self, status_code):
        """test HTTP request is successful"""
        self.assertEqual(status_code, 200)