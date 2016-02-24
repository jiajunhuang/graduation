# coding=utf-8

import tornado.web
import tornado.gen
from models.orm import ORMSession
from utils.cache import cached_property
from utils.check import require_instance
from models.user import User
from models.food import Food
from models.deal import Deal


class BaseHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def prepare(self):
        from models.orm import ORMBase, engine
        ORMBase.metadata.create_all(engine)

    @cached_property
    def orm_session(self):
        return ORMSession(autoflush=True)

    def get_current_user(self):
        try:
            return int(self.get_secure_cookie("logined").decode())
        except AttributeError:
            return None

    def on_finish(self):
        if hasattr(self, "orm_session"):
            self.orm_session.close()

    def write(self, chunk):
        if isinstance(chunk, dict):
            if "status" not in chunk:
                chunk.update(dict(
                    status=0,
                    msg="success",
                ))
        super().write(chunk)

    @require_instance(User)
    def _get_user_info(self, user):
        result = dict(
            avatar=user.avatar.decode("utf-8"),
            name=user.name.decode("utf-8"),
        )

        # 这里没有用@require_login装饰，是因为用户信息区分简略和详细版
        # 但不要求登录
        _uid = self.get_current_user()
        if _uid == user.id:
            addresses=(user.addresses.decode("utf-8")).split(";")
            result.update(dict(
                register_at=str(user.register_at),
                phone=user.phone.decode("utf-8"),
                addresses=[] if addresses == [""] else addresses
            ))
        return result

    @require_instance(Food)
    def _get_food_info(self, food):
        return dict(
            fid=food.id,
            image=food.image.decode("utf-8"),
            name=food.name.decode("utf-8"),
            seller=food.seller,
            create_at=str(food.create_at),
            price=food.price,
        )

    @require_instance(Deal)
    def _get_deal_info(self, deal):
        return dict(
            did=deal.id,
            seller=self._get_user_info(deal.seller),
            buyer=self._get_user_info(deal.buyer),
            address=deal.address.decode("utf-8"),
            phone=deal.phone.decode("utf-8"),
            sell_at=str(deal.sell_at),
            food=self._get_food_info(deal.food),
        )
