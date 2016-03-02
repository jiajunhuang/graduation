# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative
from config import Config


@as_declarative()
class ORMBase(object):
    """
    Reference:
        https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/ext/declarative/api.py#L336
    """
    __table_args__ = dict(mysql_charset="utf8")  # 默认utf-8


engine = create_engine(
    "mysql://{}:{}@{}/{}?charset=utf8&use_unicode=0".format(
        Config().mysql["user"],
        Config().mysql["password"],
        Config().mysql["host"],
        Config().mysql["db"],
        echo=True,
    )
)

ORMSession = sessionmaker(bind=engine)
