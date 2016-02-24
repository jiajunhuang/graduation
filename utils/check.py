# coding=utf-8

from models.user import User


def require_user_level(level):
    def real_decorator(func):
        def wrapper(obj, uid):
            uid = int(uid)
            user = User.get_instance_by_id(obj.orm_session, uid)

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
            logined = obj.get_current_user()
            logined = logined.decode("utf-8") if logined else False

            if logined and user.id == int(logined):
                obj._logined = int(logined)
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
