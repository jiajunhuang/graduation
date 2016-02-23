# coding=utf-8

from .base import BaseHandler
from models.goods import Goods
from models.users import Users


def require_user_level(level):
    def real_decorator(func):
        def wrapper(obj, uid):
            user = Users.get_user_info(obj.orm_session, uid)
            obj.seller = user
            if user.level == level:
                return func(obj, uid)
            else:
                obj.write(dict(
                    status=1,
                    msg='user level error',
                ))
        return wrapper
    return real_decorator


class GoodsHandler(BaseHandler):
    def get(self, uid):
        uid = int(uid)

        goods = list(map(self._get_good_info, Goods.get_goods_by_seller(self.orm_session, uid)))

        self.write(dict(
            status=0,
            msg="success",
            goods=goods,
        ))

    @require_user_level(level=1)
    def post(self, uid):
        image = self.get_argument("image", "")
        name = self.get_argument("name")
        price = float(self.get_argument("price", 0))
        seller = self.seller.id

        good = Goods(
            image=image,
            name=name,
            seller=seller,
            price=price,
        )

        self.orm_session.add(good)
        self.orm_session.commit()
        self.orm_session.refresh(good)

        self.write(dict(
            status=1,
            msg="success",
            gid=good.id,
        ))
