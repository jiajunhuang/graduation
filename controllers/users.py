# coding=utf-8

from .base import BaseHandler
from models.users import Users


class UserHandler(BaseHandler):
    """获取用户信息"""
    def get(self, uid):
        uid = int(uid)
        user = Users.get_user_info(self.orm_session, uid)
        logined = self.get_current_user()
        if user:
            if not logined:
                result = dict(
                    status=0,
                    msg="success",
                    avatar=user.avatar.decode("utf-8"),
                    name=user.name.decode("utf-8"),
                )
            else:
                result.update(dict(
                    register_at=user.register_at,
                    phone=user.phone.decode("utf-8"),
                    address=[adrs for adrs in user.addresses.split(";")],
                ))
            self.write(result)
        else:
            self.write(dict(
                status=1,
                msg="no such user",
            ))


class RegisterHandler(BaseHandler):
    def post(self):
        level = int(self.get_argument("level", 0))
        phone = self.get_argument("phone")
        passwd = self.get_argument("passwd")
        name = self.get_argument("name", phone)

        user = Users(
            level=level,
            phone=phone,
            passwd=passwd,
            name=name,
        )
        self.orm_session.add(user)
        self.orm_session.commit()

        user = Users.get_user_by_phone(self.orm_session, phone)
        if user:
            self.set_secure_cookie("logined", phone)
            self.write(dict(
                status=0,
                msg="success",
                uid=user.id,
            ))
        else:
            self.write(dict(
                status=1,
                msg="create new user failed",
            ))
