from flask import request, g
from flaskblog import create_app
from time import time

app = create_app()
# TODO report on all failed tests, not only first failure

# global test parameters
test_count = 0
tests_duration = 0.0

# helper decorator functions
def context_test(test):
    def inner():
        global test_count
        test_count += 1
        test()
    return inner

def time_function(fun):
    def inner():
        start = time()
        fun()
        end = time()
        global tests_duration
        tests_duration = end - start

    return inner

# test functions
@context_test
def test_routes():
    with app.test_request_context('/'):
        assert request.path == '/'


@time_function
def all_tests():
    test_routes()

if __name__ == '__main__':
    try:
        all_tests()
    except Exception as err:
        print('context test error occurred')
        print('-' * 70)
        raise err
    else:
        print('-' * 70)
        print('ran %d tests in %f seconds' % (test_count, tests_duration))
        print('\nOK')