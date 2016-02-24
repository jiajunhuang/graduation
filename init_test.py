# coding=utf-8

import random
import tornado.ioloop
import tornado.web

from models.user import User
from models.food import Food
from models.deal import Deal

from tornado.options import define
define("debug", default=False, help="debug=True|False")
define("port", default=8888, help="port=8888")
tornado.options.parse_command_line()


def main():
    from models.orm import ORMSession, ORMBase, engine
    ORMBase.metadata.create_all(engine)
    orm_session = ORMSession(autoflush=True)

    # add user
    phone_base = 9999
    for i in range(10):
        user = User(
            phone=phone_base + i,
            passwd="123456",
            level=random.choice([1, 2, 0]),
            name=random.choice(["jhone", "张三", 'lisi', "a*b", "1@2"]),
            addresses=random.choice(["上海;北京", ""]),
        )
        orm_session.add(user)
        orm_session.commit()
    orm_session.add(User(  # 卖家
        phone=99999,
        passwd="123456",
        name="99999",
        level=1,
    ))
    orm_session.add(User(  # 管理员
        phone=88888,
        passwd="123456",
        name="88888",
        level=2,
    ))

    # add food
    for i in range(10):
        food = Food(
            name=random.choice(["炸酱面", "noddles", "rice", "烤鸭", "好吃的"]),
            seller=11,
            price=random.choice([0, 1.11, 2.22])
        )
        orm_session.add(food)
        orm_session.commit()

    # add deal
    for i in range(10):
        deal = Deal(
            seller=99999,
            buyer=random.choice([1, 2, 3, 4]),
            food=random.choice([1, 2, 3, 4, 5]),
            address=random.choice(["上海", "USA"]),
            phone="10086",
        )
        orm_session.add(deal)
        orm_session.commit()


if __name__ == "__main__":
    main()
