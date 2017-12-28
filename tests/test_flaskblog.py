import os
import flaskblog
import unittest
import tempfile

class FlaskblogTestCase(unittest.TestCase):

    def setUp(self):
        flaskblog.app.testing = True
        self.db_fd, flaskblog.app.config['DATABASE'] = tempfile.mkstemp() # initialize new database
        self.app = flaskblog.app.test_client() # create test client
        with flaskblog.app.app_context():
            flaskblog.db_manager.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskblog.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
