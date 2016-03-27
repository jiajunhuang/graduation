# coding=utf-8

from .base import BaseHandler
from models.deal import Deal
from utils.check import require_login


class DealHandler(BaseHandler):
    @require_login
    def get(self, uid):
        """
        @apiDescription 获取某uid的交易信息
        @api {get} "/user/([0-9]+)/deals/?" 获取交易信息
        @apiGroup deal

        @apiPermission user

        @apiSuccess {Array} deals 交易信息，如下:
        @apiSuccess {Number} did 交易id
        @apiSuccess {JSON} seller 卖家信息
        @apiSuccess {JSON} buyer 买家信息
        @apiSuccess {String} address 配送地址
        @apiSuccess {String} phone 号码
        @apiSuccess {String} sell_at 销售时间
        @apiSuccess {JSON} food 食品信息
        @apiSuccessExample {json} Success Response:
        {
            "deals": [
                {
                "phone": "10086",
                "seller": {
                    "addresses": [],
                    "register_at": "1456317626",
                    "name": "99999",
                    "phone": "99999",
                    "avatar": ""
                },
                "buyer": {
                    "addresses": [],
                    "register_at": "1456317626",
                    "name": "99999",
                    "phone": "99999",
                    "avatar": ""
                },
                "food": {
                    "fid": 5,
                    "price": 1.11,
                    "create_at": "1456317627",
                    "seller": 11,
                    "name": "好吃的",
                    "image": ""
                },
                "sell_at": "1456317627",
                "address": "USA",
                "did": 10
                }
            ],
        }
        """
        uid = int(uid)
        deals = Deal.get_deals_by_uid(self.orm_session, uid)
        deals = list(map(self._get_deal_info, deals))
        self.write(dict(
            deals=deals
        ))

    @require_login
    def post(self, uid):
        """
        @apiDescription 增加交易
        @api {post} "/user/([0-9]+)/deals/?" 增加新的交易
        @apiGroup deal

        @apiParam {Number} seller 买家
        @apiParam {Number} fid 食品id
        @apiParam {String} address 配送地址
        @apiParam {String} phone 手机号

        @apiPermission user

        @apiSuccess {Number} did 交易订单号
        """
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
        """
        @apiDescription 删除交易
        @api {delete} "/user/([0-9]+)/deals/?" 删除交易
        @apiGroup deal

        @apiParam {Number} did 交易订单号

        @apiPermission user
        """
        did = int(self.get_argument("did"))
        Deal.delete(self.orm_session, did)
        self.write({})
