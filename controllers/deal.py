# coding=utf-8

from .base import BaseHandler
from models.deal import Deal
from utils.check import require_login


class DealHandler(BaseHandler):
    @require_login
    def get(self, uid):
        uid = int(uid)
        deals = Deal.get_deals_by_uid(self.orm_session, uid)
        deals = list(map(self._get_deal_info, deals))
        self.write(dict(
            deals=deals
        ))

    @require_login
    def post(self, uid):
        seller = int(self.get_argument("seller"))
        fid = int(self.get_argument("food"))
        address = self.get_argument("address")
        phone = self.get_argument("phone")

        deal = Deal(
            seller=seller,
            buyer=uid,
            food=fid,
            address=address,
            phone=phone,
        )

        self.orm_session.add(deal)
        self.orm_session.commit()

        self.write(dict(
            deal=deal.id,
        ))

    @require_login
    def delete(self, uid):
        did = int(self.get_argument("did"))
        Deal.delete(self.orm_session, did)
        self.write({})
