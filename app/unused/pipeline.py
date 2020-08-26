"""
This is example of middleware pattern
"""

from abc import ABC


def middleware_foo(get_response):
    def middleware(request):
        print('pre_foo')
        response = get_response(request)
        print('post_foo')
        return response
    return middleware


def middleware_bar(get_response):
    def middleware(request):
        print('pre_bar')
        response = get_response(request)
        print('post_bar')
        return response
    return middleware


def middleware_baz(get_response):
    def middleware(request):
        print('pre_baz')
        response = get_response(request)
        print('post_baz')
        return response
    return middleware


class BaseRequestPipeline(ABC):
    middlewares = []

    def prepare_request(self):
        """ Init request """
        request = dict()
        return request

    def execute_request(self, request):
        """ Sending request """
        print('execute_request')
        response = request
        return response

    def prepare_pipeline(self):
        """ Closure middlewares """
        get_response = self.execute_request

        for middleware_item in self.middlewares[::-1]:
            middleware = middleware_item(get_response)
            get_response = middleware

        return get_response

    def send(self):
        pipeline = self.prepare_pipeline()
        request = self.prepare_request()
        result = pipeline(request)

        return result


class ExampleRequestPipeline(BaseRequestPipeline):
    middlewares = [
        middleware_foo,
        middleware_bar,
        middleware_baz,
    ]


request_pipeline = ExampleRequestPipeline()
validated_data = request_pipeline.send()
