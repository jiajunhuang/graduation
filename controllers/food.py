# coding=utf-8

from .base import BaseHandler
from models.food import Food
from models.user import User
from utils.check import require_user_level, require_login


class FoodHandler(BaseHandler):
    def get(self, uid):
        """
        @apiDescription 获取uid所提供的食品
        @api {get} /user/([0-9]+)/foods/? 获取某uid提供的食品
        @apiGroup food

        @apiPermission user

        @apiSuccess {Array} foods 某uid所提供的食品信息，格式如下:
        @apiSuccess {Number} fid 食品id
        @apiSuccess {String} image 图片路径
        @apiSuccess {String} name 食品名称
        @apiSuccess {JSON} seller 用户信息, 见获取用户信息API
        @apiSuccess {String} create_at 创建时间
        @apiSuccess {Number} price 食品价格
        @apiSuccess {Array} grades 评价的array
        @apiSuccess {Number} avg_grade 平均评分，如果没有评论则取4分

        @apiSuccessExample {json} Success Response:
        {
            "foods": [
                {
                    "fid": 4,
                    "price": 0,
                    "create_at": "1456317627",
                    "seller": 11,
                    "name": "炸酱面",
                    "image": ""
                },
                ...
            ],
        }
        """
        uid = int(uid)

        foods = list(map(self._get_food_info, Food.get_food_by_seller(self.orm_session, uid)))

        self.write(dict(
            foods=foods,
        ))

    @require_user_level(level=1)
    @require_login
    def post(self, uid):
        """
        @apiDescription 创建食品
        @api {post} /user/([0-9]+)/foods/? 创建食品
        @apiGroup food

        @apiParam {String} image 食品图片
        @apiParam {String} name 食品名称
        @apiParam {Number} price 食品价格

        @apiPermission seller

        @apiSuccess {Number} fid 食品id
        """
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
    @require_login
    def delete(self, uid):
        """
        @apiDescription 删除食品
        @api {delete} /user/([0-9]+)/foods/? 删除
        @apiGroup food

        @apiParam {Number} fid 食品id

        @apiPermission seller
        """
        uid = int(uid)
        user = User.get_instance_by_id(self.orm_session, uid)
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
    @require_login
    def put(self, uid):
        """
        @apiDescription 修改食品
        @api {put} /user/([0-9]+)/foods/? 修改
        @apiGroup food

        @apiParam {Number} fid 食品id
        @apiParam {String} [image] 照片地址
        @apiParam {String} [name] 食品名称
        @apiParam {Number} [seller] 卖家
        @apiParam {Number} [price] 价格

        @apiPermission seller
        """
        fid = int(self.get_argument("fid"))
        food = Food.get_instance_by_id(self.orm_session, fid)

        to_change = {
            "image": self.get_argument("image", None),
            "name": self.get_argument("name", None),
            "seller": int(self.get_argument("seller", 0)),
            "price": float(self.get_argument("price", 0)),  # TODO maybe bug because of precision
        }

        for key, value in to_change.items():
            if value:
                setattr(food, key, value)
        self.orm_session.commit()
        self.write({})
