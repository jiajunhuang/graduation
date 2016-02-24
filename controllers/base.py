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

    def write(self, chunk):
        if isinstance(chunk, dict):
            if not hasattr(chunk, "status"):
                chunk.update(dict(
                    status=0,
                    msg="success",
                ))
        super().write(chunk)

    def _get_user_info(self, user, logined=False):
        result = dict(
            avatar=user.avatar.decode("utf-8"),
            name=user.name.decode("utf-8"),
        )
        if logined:
            addresses=(user.addresses.decode("utf-8")).split(";")
            result.update(dict(
                register_at=user.register_at.strftime("%s"),
                phone=user.phone.decode("utf-8"),
                addresses=[] if addresses == [""] else addresses
            ))
        return result

    def _get_good_info(self, good):
        return dict(
            id=good.id,
            image=good.image.decode("utf-8"),
            name=good.name.decode("utf-8"),
            seller=good.seller,
            create_at=good.create_at.strftime("%s"),
            price=good.price,
        )
