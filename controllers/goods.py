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

        goods = []
        for good in Goods.get_goods_by_seller(self.orm_session, uid):
            goods.append(dict(
                id=good.id,
                image=good.image,
                name=good.name,
                seller=good.seller,
                create_at=good.create_at,
                price=good.price,
            ))

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

        goods = Goods.get_goods_by_seller(self.orm_session, uid)

        try:
            good = goods[0]
            self.write(dict(
                status=1,
                msg="success",
                gid=good.id,
            ))
        except IndexError:
            self.write(dict(
                status=1,
                msg='failed to add a good',
            ))
