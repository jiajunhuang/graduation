# coding=utf-8

import tornado.ioloop
import tornado.web

from controllers.index import IndexHandler
from controllers.file_upload import FileHandler
from controllers.users import UserHandler, RegisterHandler
from config import Config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload/?", FileHandler),
            (r"/user/([0-9]+)/?", UserHandler),
            (r"/user/new/?", RegisterHandler),
        ]
        settings = {
            "template_path": Config().template_path,
            "static_path": Config().static_path,
            "cookie_secret": "hcfHo1VmQ8z9kut.wMVwympjbM",
            "debug": True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
