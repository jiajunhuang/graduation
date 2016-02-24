# coding=utf-8

from models.user import User
from models.food import Food


def require_user_level(level):
    def real_decorator(func):
        def wrapper(obj, uid):
            uid = int(uid)
            user = User.get_instance_by_id(obj.orm_session, uid)

            if user:
                return func(obj, uid)
            else:
                obj.write(dict(
                    status=1,
                    msg="please login"
                ))
                return

            obj.seller = user
            if user.level == level:
                return func(obj, uid)
            else:
                obj.write(dict(
                    status=1,
                    msg="user level error",
                ))
                return
        return wrapper
    return real_decorator


def require_login(func):
    def wrapper(obj, uid):
            uid = int(uid)
            user = User.get_instance_by_id(obj.orm_session, uid)

            if user:
                return func(obj, uid)
            else:
                obj.write(dict(
                    status=1,
                    msg="please login"
                ))
                return
    return wrapper


def require_instance(atype):
    def real_decorator(func):
        def wrapper(obj, instance):
            if not isinstance(instance, atype):
                instance = atype.get_instance_by_id(obj.orm_session, instance)
                if not instance:
                    return dict(
                        status=1,
                        msg="no such item",
                    )

            return func(obj, instance)
        return wrapper
    return real_decorator


def check_fid(func):
    def wrapper(obj):
        fid = int(obj.get_argument("fid"))
        food = Food.get_instance_by_id(int(fid))
        if not food:
            obj.write(dict(
                status=1,
                msg="no such food",
            ))
            return
        obj._food = food
        return func(obj)
    return wrapper
