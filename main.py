import tornado.ioloop
import tornado.web
import tornado.autoreload
import tornado.httpserver
import os
from moudle.handler.mainhandler import *

template_path=os.path.join(os.path.dirname(__file__), "template")

print template_path
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
    "template_path":template_path,
}


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/com",ShequHandler),
], **settings)

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8888)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()