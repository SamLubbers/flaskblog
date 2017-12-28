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

    def test_empty_db(self):
        res = self.app.get('/')
        assert b'no entries to show' in res.data

    def login(self, username, password):
        return self.app.post('/login',
                             data=dict(username=username,
                                       password=password),
                             follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        # correct login
        res = self.login('admin', 'default')
        assert b'log out' in res.data
        assert b'New blog' in res.data
        # correct log out
        res = self.logout()
        print(res.data)
        assert b'log in' in res.data
        # login wrong username
        res = self.login('adminn', 'default')
        assert b'invalid username' in res.data
        # login wrong password
        self.logout()
        res = self.login('admin', 'defaul')
        assert b'invalid password' in res.data

if __name__ == '__main__':
    unittest.main()
