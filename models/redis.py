# coding=utf-8

import redis
from config import Config

host, port = Config().redis
RedisSession = redis.StrictRedis(host=host, port=port)
