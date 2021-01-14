from werkzeug.wrappers import Request, Response

# AuthMiddleware
class AuthMiddleware():
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        print("Middleware is Called.......!")
        print(request.headers)
        return self.app(environ, start_response)