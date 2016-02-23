# coding=utf-8

"""用户表"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from .orm import ORMBase


class Users(ORMBase):
    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    avatar = Column(String(1024), nullable=False, default="")  # 头像路径
    level = Column(Integer, nullable=False, default=0, index=True)  # 用户级别，0为普通用户，1为商家，2为管理员
    phone = Column(String(11), nullable=False, index=True)  # 注册手机号码
    name = Column(String(24), nullable=False, index=True)  # 用户名
    register_at = Column(DateTime, nullable=False, default=datetime.datetime.now())  # 注册时间，只要插入一次，所以用now()而不是now
    addresses = Column(String(4096), nullable=False, default="")  # 配送地址，用';'分隔
    is_deleted = Column(Boolean, nullable=False, default=False)  # 用户是否删除
