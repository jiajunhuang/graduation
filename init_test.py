# coding=utf-8

import os
import tornado.ioloop
import tornado.web

from models.user import User  # noqa
from models.food import Food  # noqa
from models.deal import Deal  # noqa
from models.grade import Grade  # noqa

from sql.mock_user import gen

from tornado.options import define
define("debug", default=False, help="debug=True|False")
define("port", default=8888, help="port=8888")
tornado.options.parse_command_line()


def main():
    from models.orm import ORMSession, ORMBase, engine
    ORMBase.metadata.create_all(engine)
    orm_session = ORMSession(autoflush=True)

    # add user
    orm_session.add(User(
        phone=15879589998,
        passwd="123456",
        level=1,
        name="我是商家",
        addresses="上海陆家嘴;北京中关村",
    ))
    orm_session.commit()
    orm_session.add(User(  # 管理员
        phone=15879589999,
        passwd="123456",
        name="我叫admin",
        level=2,
    ))

if __name__ == "__main__":
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    # first, create db
    CREATE_DB = "mysql < %s" % os.path.join(CURRENT_DIR, "sql/create_db.sql")
    os.system(CREATE_DB)
    # insert some pre-defined data
    main()
    # insert random generate data
    INSERT_RANDOM_DATA = "mysql -u root < %s" % os.path.join(CURRENT_DIR, "sql/gen_mock.sql")
    os.system(INSERT_RANDOM_DATA)

    gen()
