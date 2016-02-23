# coding=utf-8

import logging
from .base import BaseHandler
from models.users import Users


class UserHandler(BaseHandler):
    """获取用户信息"""
    def get(self, uid):
        uid = int(uid)
        user = Users.get_user_info(self.orm_session, uid)
        logined = self.get_current_user()
        if user:
            result = dict(
                status=0,
                msg="success",
                avatar=user.avatar.decode("utf-8"),
                name=user.name.decode("utf-8"),
            )
            if logined:
                addresses=(user.addresses.decode("utf-8")).split(";")
                result.update(dict(
                    register_at=user.register_at.strftime("%s"),
                    phone=user.phone.decode("utf-8"),
                    addresses=[] if addresses == [""] else addresses
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

        try:
            user = Users(
                level=level,
                phone=phone,
                passwd=passwd,
                name=name,
            )
            self.orm_session.add(user)
            self.orm_session.commit()
            self.orm_session.refresh(user)

            self.set_secure_cookie("logined", phone)
            self.write(dict(
                status=0,
                msg="success",
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
