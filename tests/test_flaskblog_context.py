from flask import request
from flaskblog import app

def test_routes():
    with app.test_request_context('/'):
        assert request.path == '/'

if __name__ == '__main__':
    try:
        test_routes()
    except AssertionError as err:
        raise Exception('context test error') from err
    else:
        print('no errors testing request context')