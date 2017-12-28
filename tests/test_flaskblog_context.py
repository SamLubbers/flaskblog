from flask import request, g
from flaskblog import app
from flaskblog.db_manager import get_db

def test_routes():
    with app.test_request_context('/'):
        assert request.path == '/'

def test_db():
    with app.test_request_context('/'):
        get_db()
        assert str(type(g.db)) == '<class \'sqlite3.Connection\'>'

if __name__ == '__main__':
    try:
        test_routes()
        test_db()
    except AssertionError as err:
        raise Exception('context test error') from err
    else:
        print('no errors when testing request context')