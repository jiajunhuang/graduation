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
    phone_base = 15879583333
    for i in range(10):
        user = User(
            phone=phone_base + i,
            passwd="123456",
            level=random.choice([1, 2, 0]),
            name=random.choice(["jhone", "张三", '李四', "王五", "swift"]),
            addresses=random.choice(["上海;北京", ""]),
        )
        orm_session.add(user)
        orm_session.commit()
    orm_session.add(User(  # 卖家
        phone=15879589998,
        passwd="123456",
        name="我叫卖家",
        level=1,
    ))
    orm_session.add(User(  # 管理员
        phone=15879589999,
        passwd="123456",
        name="我叫admin",
        level=2,
    ))

    # add food
    for i in range(10):
        food = Food(
            name=random.choice(["炸酱面", "noddles", "rice", "烤鸭", "肯打鸡"]),
            seller=11,
            price=random.choice([0, 1.11, 2.22])
        )
        orm_session.add(food)
        orm_session.commit()

    # add deal
    for i in range(10):
        deal = Deal(
            seller=random.choice(list(range(1, 10))),
            buyer=random.choice(list(range(1, 10))),
            food=random.choice(list(range(1, 10))),
            address=random.choice(["上海", "北京"]),
            phone=random.choice(["15879583333", "15879583334", "15879583335"]),
        )
        orm_session.add(deal)
        orm_session.commit()


if __name__ == "__main__":
    main()
