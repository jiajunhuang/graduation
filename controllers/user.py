# coding=utf-8

import logging
from .base import BaseHandler
from models.user import User


class UserHandler(BaseHandler):
    """获取用户信息"""
    def get(self, uid):
        uid = int(uid)
        user = User.get_user_by_id(self.orm_session, uid)
        logined = self.get_current_user()
        if user:
            result = self._get_user_by_id(user, logined)
            self.write(result)
        else:
            self.write(dict(
                status=1,
                msg="no such user",
            ))

    def delete(self, uid):
        logined = self.get_current_user()
        if logined:
            User.delete_user(self.orm_session, logined)
        self.write({})


class RegisterHandler(BaseHandler):
    def post(self):
        level = int(self.get_argument("level", 0))
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
