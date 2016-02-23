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
            self.write(dict(
                status=0,
                msg="success",
            ))
        else:
            self.write(dict(
                status=1,
                msg="login failed, user not exists or password is wrong"
            ))
