# coding:utf-8

import os
from utils.singleton import Singleton


class Config(object, metaclass=Singleton):
    __mysql_mapper = {
        "dev": {
            "host": "127.0.0.1",
            "db": "graduation",
            "user": "root",
            "password": "",
        }
    }

    __dir_path = os.path.dirname(__file__)

    def __init__(self, config_type="dev"):
        self.config_type = config_type
        self.debug = False
        self.mysql = self.__mysql_mapper[config_type]
        self.template_path = os.path.join(self.__dir_path, "templates")
        self.static_path = os.path.join(self.__dir_path, "static")
        self.img_path = os.path.join(self.static_path, "img")
