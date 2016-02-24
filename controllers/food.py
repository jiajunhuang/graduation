# coding=utf-8

import logging
from .base import BaseHandler
from models.food import Food
from models.user import User
from utils.check import require_user_level


class FoodHandler(BaseHandler):
    def get(self, uid):
        uid = int(uid)

        food = list(map(self._get_food_info, Food.get_Food_by_seller(self.orm_session, uid)))

        self.write(dict(
            food=food,
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
        self.orm_session.refresh(Food)

        self.write(dict(
            status=1,
            msg="success",
            gid=food.id,
        ))

    @require_user_level(level=1)
    def delete(self, uid):
        uid = int(uid)
        user = User.get_user_by_id(self.orm_session, uid)
        gid = int(self.get_argument("gid"))
        if not user:
            logging.debug("user does not exist")
            self.write({})
            return

        Food.delete(self.orm_session, user.id, gid)
        self.write({})
