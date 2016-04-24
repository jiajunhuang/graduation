# coding=utf-8

from .base import BaseHandler
from models.deal import Deal
from models.user import User
from models.food import Food


class AdminHandler(BaseHandler):
    def prepare(self):
        self.__category_mapper = {
            "deals": self._get_deal_info,
            "users": self._get_user_info,
            "foods": self._get_food_info,
        }

        self.__class_mapper = {
            "deals": Deal,
            "users": User,
            "foods": Food,
        }
        super().prepare()

    def get(self, category=None):
        if not self.is_admin:
            self.redirect("/login")
            return
        category = "deals" if not category else category
        if category not in ("deals", "users", "foods"):
            self.redirect("/")  # redirect for security
            return
        items = map(self.__category_mapper[category], self.__class_mapper[category].get_all_items(self.orm_session, count=100))
        self.render("admin/{}.html".format(category), active=category, items=items, sid=self.sid)
