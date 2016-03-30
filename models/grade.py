# coding=utf-8

"""商品"""

import datetime
from sqlalchemy import Column, String, Integer, DateTime, Float, desc
from sqlalchemy.sql import func
from .orm import ORMBase


class Grade(ORMBase):
    __tablename__ = "grade"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    fid = Column(Integer, nullable=False, index=True)  # 食品id
    uid = Column(Integer, nullable=False)  # 评价人
    score = Column(Float, nullable=False, default=5.00)  # 食品评分
    score_at = Column(DateTime, nullable=False, default=datetime.datetime.now)  # 评价时间
    comment = Column(String(4096), nullable=False, default="")  # 评论
    speed = Column(Integer, nullable=False, default=20)  # 配送速度

    @classmethod
    def get_last_n_items(cls, session, fid, num=30):
        return session.query(Grade).filter(
            Grade.fid == int(fid)
        ).order_by(desc(Grade.score_at)).limit(num)

    @classmethod
    def get_avg(cls, session, fid):
        return session.query(func.avg(Grade.score)).filter(
            Grade.fid == int(fid)
        ).first()

    @classmethod
    def delete(cls, session, uid, gid):
        session.query(Grade).filter(
            Grade.uid == int(uid),
            Grade.id == int(gid),
        ).delete()
        session.commit()
