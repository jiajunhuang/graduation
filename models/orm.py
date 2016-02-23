# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config


ORMBase = declarative_base()


engine = create_engine(
    "mysql://{}:{}@{}/{}?charset=utf8&use_unicode=0".format(
        Config().mysql["user"],
        Config().mysql["password"],
        Config().mysql["host"],
        Config().mysql["db"],
        echo=False,
    )
)

ORMSession = sessionmaker(bind=engine)
