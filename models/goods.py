# coding=utf-8

"""商品"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Float
from .orm import ORMBase


class Goods(ORMBase):
    __tablename__ = "goods"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)  # 商品名称
    seller = Column(Integer, nullable=False, index=True)  # 售卖者
    create_at = Column(DateTime, nullable=False, default=datetime.datetime.now())  # 上架时间
    price = Column(Float, nullable=False, default=0.00, pricision=2)  # 价格
    is_deleted = Column(Boolean, nullable=False, default=False)  # 商品是否被删除
