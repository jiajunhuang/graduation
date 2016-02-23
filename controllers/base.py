# coding=utf-8

import tornado.web
import tornado.gen
from models.orm import ORMSession
from utils.cache import cached_property


class BaseHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def prepare(self):
        from models.users import Users
        from models.goods import Goods
        from models.deals import Deals
        from models.orm import ORMBase, engine
        ORMBase.metadata.create_all(engine)

    @cached_property
    def orm_session(self):
        return ORMSession(autoflush=True)

    def get_current_user(self):
        return self.get_secure_cookie("logined")

    def on_finish(self):
        if hasattr(self, "orm_session"):
            self.orm_session.close()
