# coding=utf-8

"""交易"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime, desc
from .orm import ORMBase


class Deal(ORMBase):
    __tablename__ = "deal"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    seller = Column(Integer, nullable=False, index=True)  # 卖家
    buyer = Column(Integer, nullable=False, index=True)  # 买家
    food = Column(Integer, nullable=False, index=True)  # 商品
    address = Column(String(64), nullable=False)  # 配送地址
    phone = Column(String(11), nullable=False)  # 联系方式
    sell_at = Column(DateTime, nullable=False, default=datetime.datetime.now)  # 售出时间

    @classmethod
    def get_deals_by_uid(cls, session, buyer):
        """获取某人的全部订单"""
        return session.query(Deal).filter(
            Deal.buyer == buyer
        ).order_by(desc(Deal.sell_at)).all()

    @classmethod
    def get_all_deals(cls, session):
        return session.query(Deal).order_by(desc(Deal.sell_at)).all()

    @classmethod
    def delete(cls, session, did):
        session.query(Deal).filter(
            Deal.id == did
        ).delete()
        session.commit()
