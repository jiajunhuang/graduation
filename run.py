# coding=utf-8

import tornado.ioloop
import tornado.web

from controllers.index import IndexHandler
from controllers.file_upload import FileHandler
from config import Config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", FileHandler)
        ]
        settings = {
            "template_path": Config().template_path,
            "static_path": Config().static_path,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
