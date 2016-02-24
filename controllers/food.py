# coding=utf-8

from .base import BaseHandler
from models.food import Food
from models.user import User
from utils.check import require_user_level, require_login


class FoodHandler(BaseHandler):
    def get(self, uid):
        uid = int(uid)

        foods = list(map(self._get_food_info, Food.get_food_by_seller(self.orm_session, uid)))

        self.write(dict(
            foods=foods,
        ))

    @require_user_level(level=1)
    @require_login
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
            gid=food.id,
        ))

    @require_user_level(level=1)
    @require_login
    def delete(self, uid):
        uid = int(uid)
        user = User.get_food_by_id(self.orm_session, uid)
        gid = int(self.get_argument("gid"))
        if not user:
            self.write(dict(
                status=1,
                msg="user not exist",
            ))
            return

        Food.delete(self.orm_session, user.id, gid)
        self.write({})
