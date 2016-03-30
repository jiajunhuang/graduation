# coding=utf-8

"""商家附加信息"""

from sqlalchemy import Column, Integer, Boolean
from .orm import ORMBase


class Seller(ORMBase):
    __tablename__ = "seller"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    uid = Column(Integer, nullable=False, index=True)  # 商家uid
    lowest_money = Column(Integer, nullable=False, default=0)  # 起送金额
    invoice = Column(Boolean, nullable=False, default=False)  # 是否开发票
    distance = Column(Integer, nullable=False)  # 距离, 假数据。。。所有人看到都一样-。-

    @classmethod
    def get_instance_by_uid(cls, session, uid):
        return session.query(Seller).filter(
            Seller.uid == int(uid)
        ).first()
