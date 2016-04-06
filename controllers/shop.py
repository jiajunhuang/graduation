# coding=utf-8

import functools
from .base import BaseHandler
from models.user import User


class ShopHandler(BaseHandler):
    """批量获取商家的信息"""
    def get(self):
        """
        @apiDescription 批量获取商家的接口，由于要展示前端的功能，所以排序交由前端完成，这个接口只是提供数据，所以只写了一种排序方案，那就是注册时间~
        @api {get} /shop/all/? 批量获取商家

        @apiGroup shop

        @apiParam {Number} [page] 分页，第几页，默认为1
        @apiParam {Number} [page_size] 该页大小, 默认为20

        @apiPermission guest

        @apiSuccess {json} shops 商家信息对象
        """
        page = int(self.get_argument("page", 1))
        page_size = int(self.get_argument("page_size", 20))
        start = (page - 1) * page_size
        shops = [shop.id for shop in User.get_shops_by_regtime(self.orm_session, start, page_size)]
        self.write(dict(
            shops=list(map(functools.partial(self._get_user_info, shop=True), shops))
        ))
