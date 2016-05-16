import requests
import random
from models.user import User
from models.seller import Seller
from models.orm import ORMSession, ORMBase, engine
from models.food import Food
ORMBase.metadata.create_all(engine)
orm_session = ORMSession(autoflush=True)

URLs = "https://www.ele.me/restapi/v4/restaurants?extras%5B%5D=food_activity&extras%5B%5D=restaurant_activity&extras%5B%5D=statistics&geohash=ws1078vc3mqb&limit=100&offset=0&type=geohash", "https://www.ele.me/restapi/v4/restaurants?extras%5B%5D=food_activity&extras%5B%5D=restaurant_activity&extras%5B%5D=statistics&geohash=wtw6hgs0t4z&limit=24&offset=24&type=geohash", "https://www.ele.me/restapi/v4/restaurants?extras%5B%5D=food_activity&extras%5B%5D=restaurant_activity&extras%5B%5D=statistics&geohash=wx4g4mgs5kr&limit=24&offset=24&type=geohash", "https://www.ele.me/restapi/v4/restaurants?extras%5B%5D=food_activity&extras%5B%5D=restaurant_activity&extras%5B%5D=statistics&geohash=ws0ee7xeysg&limit=24&offset=24&type=geohash"

Foods = "https://www.ele.me/restapi/v4/restaurants/{}/mutimenu"


def gen():
    for url in URLs:
        results = requests.get(url).json()
        for result in results:
            user = User(avatar="http://fuss10.elemecdn.com/" + result["image_path"], level=1, passwd="123456", phone=result["phone"], name=result["name"], addresses=result["address"])
            orm_session.add(user)
            orm_session.commit()
            seller = Seller(uid=user.id, lowest_money=result["float_minimum_order_amount"], invoice=False, distance=result["distance"])
            orm_session.add(seller)
            orm_session.commit()

            for item in requests.get(Foods.format(result["id"])).json():
                try:
                    for food in item["foods"]:
                        f = Food(image=food["image_path"], name=food["name"], seller=user.id, price=random.choice(list(range(10, 20))))
                        orm_session.add(f)
                        orm_session.commit()
                except TypeError:
                    pass
