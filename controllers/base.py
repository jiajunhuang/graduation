# coding=utf-8

import datetime
import random

import tornado.web
import tornado.gen
from models.orm import ORMSession
from models.redis import RedisSession
from utils.cache import cached_property
from utils.check import require_instance
from models.user import User
from models.food import Food
from models.deal import Deal
from models.grade import Grade
from models.seller import Seller


class BaseHandler(tornado.web.RequestHandler):
    """
    @apiDescription 服务器返回请求字段
    @api {get} / 服务器返回请求字段
    @apiGroup base

    @apiSuccess {json} JSON 所有请求都会包含的字符
    @apiSuccessExample {json} Success Response:
    {
        "status": 0, // 0 成功，1 失败
        "msg": "xxx", // 描述信息
        "sid": "xxxRTYU&*^(*)" // session id
    }
    """
    @tornado.gen.coroutine
    def prepare(self):
        from models.orm import ORMBase, engine
        ORMBase.metadata.create_all(engine)
        self.sid = self.get_secure_cookie("sid")
        self.sid = self.sid.decode("utf-8") if self.sid else self.get_argument("sid", self.gen_sid())

    def gen_sid(self, uid=""):
        ip = self.request.remote_ip
        uid = str(uid)
        return ";".join([ip, uid])

    @cached_property
    def orm_session(self):
        return ORMSession(autoflush=True)

    @cached_property
    def redis_session(self):
        return RedisSession

    def get_current_user(self):
        uid, level = self._get_current_user_info()
        return int(uid) if uid else None

    def _get_current_user_info(self):
        server_sid = self.redis_session.get(bytes(self.sid, "utf-8"))
        if not server_sid:
            return None, None
        uid, level = server_sid.decode("utf-8").split(";")  # 只信任服务端数据
        return uid, level

    def get_current_level(self):
        uid, level = self._get_current_user_info()
        return int(level) if level else None

    @property
    def is_admin(self):
        try:
            level = self.get_current_level()
            return True if level and level ==2 else False
        except AttributeError:
            return False

    def on_finish(self):
        if hasattr(self, "orm_session"):
            self.orm_session.close()

    def write(self, chunk):
        if isinstance(chunk, dict):
            if "status" not in chunk:
                chunk.update(dict(
                    status=0,
                    msg="success",
                    sid=self.sid,
                ))
        super().write(chunk)

    @require_instance(User)
    def _get_user_info(self, user, shop=False):
        result = dict(
            uid=user.id,
            avatar=user.avatar.decode("utf-8") or self.static_url("avatar.jpg"),
            name=user.name.decode("utf-8"),
        )

        # 这里没有用@require_login装饰，是因为用户信息区分简略和详细版
        # 但不要求登录
        _uid = self.get_current_user()
        if self.is_admin or shop:
            now = datetime.datetime.now()
            last_week = now - datetime.timedelta(days=7)
            result.update(dict(
                new_seller=user.register_at > last_week,
                speed=random.choice(list(range(20, 50))),
                avg_grade=random.choice(list(range(3, 5))),
                sales_count=random.choice(list(range(30))),
                lowest_money=random.choice([0, 20, 30, 50]),  # 起送价格
                invoice=random.choice([True, False]),  # 是否开发票
                distance=random.choice(list(range(100, 10000))),  # 米
                free_send=random.choice([True, False]),  # 是否免费配送
            ))

        if self.is_admin or _uid == user.id:
            addresses=(user.addresses.decode("utf-8")).split(";")
            result.update(dict(
                level=int(user.level),
                register_at=str(user.register_at),
                phone=user.phone.decode("utf-8"),
                addresses=[] if addresses == [""] else addresses
            ))
        return result

    @require_instance(Food)
    def _get_food_info(self, food):
        fid=food.id
        return dict(
            fid=fid,
            image=food.image.decode("utf-8"),
            name=food.name.decode("utf-8"),
            seller=self._get_user_info(food.seller),
            create_at=str(food.create_at),
            price=food.price,
            grades=self._get_grade_info(fid),
            avg_grade=random.choice(list(range(3, 5)))
        )

    @require_instance(Deal)
    def _get_deal_info(self, deal):
        return dict(
            did=deal.id,
            seller=self._get_user_info(deal.seller),
            buyer=self._get_user_info(deal.buyer),
            address=deal.address.decode("utf-8"),
            phone=deal.phone.decode("utf-8"),
            sell_at=str(deal.sell_at),
            food=self._get_food_info(deal.food),
        )

    def _get_grade_info(self, fid, num=30):
        """获取食品评论和评分
        @apiDescription 评分
        @api {get} / 评分的字段
        @apiGroup grade

        @apiSuccess {Number} gid 评分id
        @apiSuccess {Number} fid 食品id
        @apiSuccess {Number} uid 评论者
        @apiSuccess {Number} seller 商家
        @apiSuccess {Number} score 评分
        @apiSuccess {String} score_at 评论时间
        @apiSuccess {String} comment 评论内容
        @apiSuccess {Number} speed 配送速度
        """
        grades = Grade.get_last_n_items(self.orm_session, fid, num)
        result = []
        for grade in grades:
            result.append(dict(
                gid=grade.id,
                fid=fid,
                uid=grade.uid,
                seller=grade.seller,
                score=grade.score,
                score_at=str(grade.score_at),
                comment=grade.comment.decode("utf-8"),
                speed=grade.speed,
            ))
        return result
