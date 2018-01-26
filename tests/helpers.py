"""functions and decorators that encapsulate common functionality reusable with multiple test cases"""
from functools import wraps
from contextlib import contextmanager
from flask import template_rendered


def client_get_request(url):
    """decorator which making requests to url and returns the
    response, loaded template and context to the test case which it decorates"""
    def decorator(test_method):
        @wraps(test_method)
        def wrapper(self):
            recorded = []

            def record(sender, template, context, **extra):
                """signals that registers the template and context when a request is made"""
                recorded.append((template, context))

            template_rendered.connect(record, self.app) # connect and register all signals
            response = self.client.get(url, follow_redirects=True) # make request

            template, context = recorded[0] # extract data recorded in previous request

            template_rendered.disconnect(record, self.app) # disconnect from signal listening

            test_method(self, response, template, context) # pass all data to the test function
        return wrapper
    return decorator
