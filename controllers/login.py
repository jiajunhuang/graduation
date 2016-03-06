# coding:utf-8

from .base import BaseHandler
from models.user import User


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        phone = self.get_argument("phone")
        passwd = self.get_argument("passwd")

        user = User.user_login(self.orm_session, phone, passwd)

        if user:
            uid = str(user.id)
            level = str(user.level)
            sid = self.gen_sid(uid)
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
