# coding=utf-8

"""用户表"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime
from .orm import ORMBase


class User(ORMBase):
    __tablename__ = "user"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    avatar = Column(String(1024), nullable=False, default="")  # 头像路径
    level = Column(Integer, nullable=False, default=0, index=True)  # 用户级别，0为普通用户，1为商家，2为管理员
    passwd = Column(String(64), nullable=False)  # 密码
    phone = Column(String(11), nullable=False, primary_key=True, unique=True)  # 注册手机号码
    name = Column(String(24), nullable=False, index=True)  # 用户名
    register_at = Column(DateTime, nullable=False, default=datetime.datetime.now)  # 注册时间，只要插入一次，所以用now()而不是now
    addresses = Column(String(4096), nullable=False, default="")  # 配送地址，用';'分隔

    @classmethod
    def get_instance_by_id(cls, session, uid):
        return session.query(User).filter(
            User.id == uid,
        ).first()

    @classmethod
    def get_user_by_phone(cls, session, phone):
        return session.query(User).filter(
            User.phone == phone,
        ).first()

    @classmethod
    def user_login(cls, session, phone, passwd):
        return session.query(User).filter(
            User.phone == phone,
            User.passwd == passwd,
        ).first()

    @classmethod
    def delete(cls, session, uid):
        user = User.get_instance_by_id(session, int(uid))
        if user:
            user.delete()
            session.commit()
