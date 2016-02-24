# coding=utf-8

from .base import BaseHandler
from models.food import Food
from models.user import User
from utils.check import require_user_level, check_fid


class FoodHandler(BaseHandler):
    def get(self, uid):
        """获取uid所提供的食品"""
        uid = int(uid)

        foods = list(map(self._get_food_info, Food.get_food_by_seller(self.orm_session, uid)))

        self.write(dict(
            foods=foods,
        ))

    @require_user_level(level=1)
    def post(self, uid):
        image = self.get_argument("image", "")
        name = self.get_argument("name")
        price = float(self.get_argument("price", 0))
        seller = self.seller.id

        food = Food(
            image=image,
            name=name,
            seller=seller,
            price=price,
        )

        self.orm_session.add(food)
        self.orm_session.commit()
        self.orm_session.refresh(food)

        self.write(dict(
            fid=food.id,
        ))

    @require_user_level(level=1)
    def delete(self, uid):
        uid = int(uid)
        user = User.get_food_by_id(self.orm_session, uid)
        fid = int(self.get_argument("fid"))
        if not user:
            self.write(dict(
                status=1,
                msg="user not exist",
            ))
            return

        Food.delete(self.orm_session, user.id, fid)
        self.write({})

    @require_user_level(level=1)
    @check_fid
    def put(self, uid):
        to_change = {
            "fid": int(self.get_argument("fid")),
            "image": self.get_argument("image", None),
            "name": self.get_argument("name", None),
            "seller": int(self.get_argument("seller", 0)),
            "price": float(self.get_argument("price", 0)),  # TODO maybe bug because of precision
        }

        for key, value in to_change.items():
            if value:
                self._food[key] = value
        self.orm_session.commit()
