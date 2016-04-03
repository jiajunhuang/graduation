# coding=utf-8

import logging
from .base import BaseHandler
from models.user import User
from utils.check import require_login


class UserHandler(BaseHandler):
    """获取用户信息"""
    def is_shop(self):
        return True if self.request.uri.startswith("/shop/") else False

    def get(self, uid):
        """
        @apiDescription 获取用户信息
        @api {get} /user/([0-9]+)/? 获取用户信息
        @apiGroup user

        @apiParam {Number} uid 用户uid

        @apiPermission user

        @apiSuccess {Number} uid 用户uid
        @apiSuccess {String} avatar 头像
        @apiSuccess {String} name 用户名
        @apiSuccess {Number} speed 配送时间，仅商家时出现
        @apiSuccess {Number} sales_count 销量，仅商家出现
        @apiSuccess {Number} lowest_money 起送价，仅商家出现
        @apiSuccess {Boolean} invoice 是否开具发票，仅商家出现
        @apiSuccess {Integer} distance 距离，仅商家出现
        @apiSuccess {Boolean} new_seller 是否为新商家，仅商家出现
        @apiSuccess {Number} level 用户级别，仅获取自己信息时出现
        @apiSuccess {String} register_at 注册时间，仅获取自己信息时出现
        @apiSuccess {String} phone 手机号，仅获取自己信息时出现
        @apiSuccess {Array} address 配送地址，仅获取自己信息时出现
        @apiSuccessExample {json} Success Response:
        {
            "uid": 1,
            "avatar": "http://xxxx.com/avatar.png",
            "name": "001",
            // 以下为用户获取自己信息时才会出现
            "level": 0,
            "register_at": "2016-03-27 00:00:00",
            "phone": "99999",
            "address": []
        }

        @apiError UserNotExists 用户不存在
        """
        uid = int(uid)
        # hack: 因为改url涉及面太广，所以通过查看self.require_shop 来判定吧-。-
        shop = self.is_shop()

        user = User.get_instance_by_id(self.orm_session, uid)
        if user:
            result = self._get_user_info(user, shop)
            self.write(result)
        else:
            self.write(dict(
                status=1,
                msg="no such user",
            ))

    @require_login
    def put(self, uid):
        """
        @apiDescription 修改用户信息
        @api {put} /user/([0-9]+)/? 修改用户信息
        @apiGroup user

        @apiParam {Number} [uid] uid
        @apiParam {Number} [level] 级别
        @apiParam {String} [passwd] 密码
        @apiParam {String} [phone] 手机号
        @apiParam {String} [name] 名字
        @apiParam {String} [address] 地址

        @apiPermission user

        @apiError UserNotExists 用户不存在
        """
        to_change = dict(
            avatar=self.get_argument("avatar", None),
            level=int(self.get_argument("level", 0)),
            passwd=self.get_argument("passwd", None),
            phone=self.get_argument("phone", None),
            name=self.get_argument("name", None),
            address=self.get_argument("addresses", None)
        )

        user = User.get_instance_by_id(self.orm_session, uid)
        if not user:
            self.write(dict(
                status=1,
                msg="user does not exists"
            ))
            return

        for key, value in to_change.items():
            if value:
                setattr(user, key, value)
        self.orm_session.commit()
        self.write()

    @require_login
    def delete(self, uid):
        """
        @apiDescription 删除用户信息
        @api {delete} /user/([0-9]+)/? 删除用户信息
        @apiGroup user

        @apiPermission user
        """
        User.delete(self.orm_session, uid)
        self.write({})


class RegisterHandler(BaseHandler):
    """
    @apiDescription 创建用户
    @api {post} /user/new 创建新用户
    @apiGroup user

    @apiParam {String} phone 手机号
    @apiParam {String} passwd 密码
    @apiParam {String} [name] 用户名，可缺省，默认为电话号码

    @apiPermission user

    @apiSuccess {Number} uid 用户uid，全局唯一

    @apiError UserExists 手机号已存在
    @apiError UserLevelError 所申请的用户级别错误
    """
    def post(self):
        level = int(self.get_argument("level", 0))
        if not 0 <= level < 2:
            self.write(dict(
                status=1,
                msg="illegal"
            ))
            return

        phone = self.get_argument("phone")
        passwd = self.get_argument("passwd")
        name = self.get_argument("name", phone)

        try:
            user = User(
                level=level,
                phone=phone,
                passwd=passwd,
                name=name,
            )
            self.orm_session.add(user)
            self.orm_session.commit()
            self.orm_session.refresh(user)

            self.write(dict(
                uid=user.id,
            ))
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.error(e)
            self.write(dict(
                status=1,
                msg="failed to register",
            ))
