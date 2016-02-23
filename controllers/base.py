# coding=utf-8

from models.orm import ORMSession
import tornado.web
import tornado.gen


class BaseHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def prepare(self):
        # from models.users import Users
        # from models.goods import Goods
        # from models.deals import Deals
        # from models.orm import ORMBase, engine
        # ORMBase.metadata.create_all(engine)
        pass

    @property
    def orm_session(self):
        return ORMSession(autoflush=True)

    def get_current_user(self):
        return self.get_secure_cookie("logined")

    def on_finish(self):
        self.orm_session.close()
