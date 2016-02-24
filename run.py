# coding=utf-8

import logging
import tornado.ioloop
import tornado.web

from controllers.index import IndexHandler
from controllers.file_upload import FileHandler
from controllers.login import LoginHandler, LogoutHandler
from controllers.user import UserHandler, RegisterHandler
from controllers.food import FoodHandler
from config import Config

from tornado.options import define, options
define("debug", default=False, help="debug=True|False")
define("port", default=8888, help="port=8888")
tornado.options.parse_command_line()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload/?", FileHandler),
            (r"/user/([0-9]+)/?", UserHandler),
            (r"/user/new/?", RegisterHandler),
            (r"/user/([0-9]+)/foods/?", FoodHandler),
            (r"/login/?", LoginHandler),
            (r"/logout/?", LogoutHandler),
        ]
        settings = {
            "template_path": Config().template_path,
            "static_path": Config().static_path,
            "cookie_secret": "hcfHo1VmQ8z9kut.wMVwympjbM",
            "debug": options.debug,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(options.port)
    logging.warn("server has been listen at port %s." % options.port)
    tornado.ioloop.IOLoop.current().start()
