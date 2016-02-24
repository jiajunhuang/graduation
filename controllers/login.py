# coding:utf-8

from .base import BaseHandler
from models.users import Users


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        phone = self.get_argument("phone")
        passwd = self.get_argument("passwd")

        user = Users.user_login(self.orm_session, phone, passwd)

        if user:
            self.set_secure_cookie("logined", phone)
        else:
            self.write(dict(
                status=1,
                msg="login failed, user not exists or password is wrong"
            ))


class LogoutHandler(BaseHandler):
    def get(self):
        phone = self.get_current_user()
        if not phone:
            return

        user = Users.get_user_by_phone(self.orm_session, phone)
        if not user:
            self.write(dict(
                status=1,
                msg="user does not exist",
            ))
            return

        self.clear_cookie("logined")
        self.write(dict(
            status=1,
            msg="success",
        ))
