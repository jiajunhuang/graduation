# coding=utf-8

"""交易"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Float
from .orm import ORMBase


class Deals(ORMBase):
    __tablename__ = "deals"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    seller = Column(Integer, nullable=False, index=True)  # 卖家
    buyer = Column(Integer, nullable=False, index=True)  # 买家
    address = Column(String(64), nullable=False)  # 配送地址
    phone = Column(String(11), nullable=False)  # 联系方式
    sell_at = Column(DateTime, nullable=False, default=datetime.datetime.now())  # 售出时间
    price = Column(Float, nullable=False, default=0.00)  # 价格
