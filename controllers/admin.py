# coding=utf-8

from .base import BaseHandler
from models.deal import Deal


class AdminHandler(BaseHandler):
    def get(self):
        deals = map(self._get_deal_info, Deal.get_all_deals(self.orm_session))
        self.render("admin.html", deals=deals)
