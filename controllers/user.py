# coding=utf-8

import logging
from .base import BaseHandler
from models.user import User
from utils.check import require_login


class UserHandler(BaseHandler):
    """获取用户信息"""
    def get(self, uid):
        uid = int(uid)
        user = User.get_instance_by_id(self.orm_session, uid)
        if user:
            result = self._get_user_info(user)
            self.write(result)
        else:
            self.write(dict(
                status=1,
                msg="no such user",
            ))

    @require_login
    def put(self, uid):
        to_change = dict(
            avatar=self.get_argument("avatar", None),
            level=int(self.get_argument("level", 0)),
            passwd=self.get_argument("passwd", None),
            phone=self.get_argument("phone", None),
            name=self.get_argument("name", None),
            address=self.get_argument("addresses", None)
        )

        user = User.get_instance_by_id(self.orm_session, uid)

        for key, value in to_change.items():
            if value:
                setattr(user, key, value)
        self.orm_session.commit()

    @require_login
    def delete(self, uid):
        User.delete(self.orm_session, uid)
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
