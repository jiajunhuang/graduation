# coding=utf-8

from .base import BaseHandler
from models.deal import Deal


class DealHandler(BaseHandler):
    def get(self, uid):
        user = self.get_current_user()
        if not user:
            self.write(dict(
                status=1,
                msg="please login",
            ))

        deals = Deal.get_deals_by_id(self.orm_session, user.uid)
        deals = map(self._get_deal_info, deals)
        self.write(dict(
            deals=deals
        ))
