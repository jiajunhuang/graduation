# coding:utf-8

from .base import BaseHandler
from models.user import User


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        """
        @apiDescription 用户登录
        @api {post} /login/? 登录
        @apiGroup login

        @apiParam {Number} phone 手机号
        @apiParam {String} passwd 密码

        @apiError UserNotExists 用户不存在
        @apiError BadPassword 密码错误
        """
        phone = self.get_argument("phone")
        passwd = self.get_argument("passwd")

        user = User.user_login(self.orm_session, phone, passwd)

        if user:
            uid = str(user.id)
            level = str(user.level)
            self.sid = sid = self.gen_sid(uid)
            self.redis_session.set(sid, ";".join([uid, level]))
            self.set_secure_cookie("sid", sid)
            if user.level == 2:
                self.redirect("/admin")
            else:
                self.write({})
        else:
            self.write(dict(
                status=1,
                msg="login failed, user not exists or password is wrong"
            ))


class LogoutHandler(BaseHandler):
    def get(self):
        """
        @apiDescription 用户登出
        @api {get} /logout/? 登出
        @apiGroup login

        @apiError UserNotLogin 用户未登录
        @apiError UserNotExists 用户不存在
        """
        _uid = self.get_current_user()
        if not _uid:
            self.write(dict(
                status=1,
                msg="user does not logined",
            ))
            return

        user = User.get_instance_by_id(self.orm_session, _uid)
        if not user:
            self.write(dict(
                status=1,
                msg="user does not exist",
            ))
            return

        self.redis_session.delete(self.sid)
        self.clear_cookie("sid")
        self.write({})


class LoginChecker(BaseHandler):
    def get(self):
        _uid = self.get_current_user()
        if _uid:
            self.write(dict(
                uid=_uid,
            ))
        else:
            self.write(dict(
                status=1,
                msg="user doesn't logined yet!"
            ))
