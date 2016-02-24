# coding=utf-8

import tornado.web
import tornado.gen
from models.orm import ORMSession
from utils.cache import cached_property


class BaseHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def prepare(self):
        from models.user import User  # NOQA
        from models.food import Food  # NOQA
        from models.deal import Deal  # NOQA
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

    def _get_food_info(self, food):
        return dict(
            id=food.id,
            image=food.image.decode("utf-8"),
            name=food.name.decode("utf-8"),
            seller=food.seller,
            create_at=food.create_at.strftime("%s"),
            price=food.price,
        )

    def _get_deal_info(self, deal):
        return dict(
            did=deal.id,
            seller=self._get_user_info(deal.seller),
            buyer=self._get_user_info(deal.buyer),
            address=deal.address,
            phone=deal.phone,
            sell_at=self.sell_at.strftime("%s"),
            food=self._get_food_info(deal.food),
        )
