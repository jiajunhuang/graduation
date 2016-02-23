# coding=utf-8

from .base import BaseHandler
from models.users import Users


class UserHandler(BaseHandler):
    """获取用户信息"""
    def get(self, uid):
        uid = int(uid)
        user = Users.get_user_info(self.orm_session)
        if user:
            self.write(dict(
                status=0,
                msg="",
                avatar=user.avatar,
                phone=user.phone,
                name=user.name,
                register_at=user.register_at,
                address=[adrs for adrs in user.addresses.split(";")],
            ))
        else:
            self.write(dict(
                status=0,
                msg="no such user",
            ))
