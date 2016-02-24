# coding=utf-8

"""商品"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float, desc
from .orm import ORMBase


class Food(ORMBase):
    __tablename__ = "food"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    image = Column(String(1024), nullable=False, default="")  # 商品图片路径
    name = Column(String(64), nullable=False)  # 商品名称
    seller = Column(Integer, nullable=False, index=True)  # 售卖者
    create_at = Column(DateTime, nullable=False, default=datetime.datetime.now())  # 上架时间
    price = Column(Float, nullable=False, default=0.00)  # 价格

    @classmethod
    def get_Food_by_seller(cls, session, uid):
        return session.query(Food).filter(
            Food.seller==uid,
        ).order_by(desc(Food.create_at)).all()

    @classmethod
    def delete(cls, session, uid, gid):
        session.query(Food).filter(
            Food.id==gid,
            Food.seller==uid,
        ).delete()
