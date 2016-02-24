# coding=utf-8

from models.user import User


def require_user_level(level):
    def real_decorator(func):
        def wrapper(obj, uid):
            user = User.get_user_by_id(obj.orm_session, uid)
            obj.seller = user
            if user.level == level:
                return func(obj, uid)
            else:
                obj.write(dict(
                    status=1,
                    msg='user level error',
                ))
                return
        return wrapper
    return real_decorator


def require_login(func):
    def wrapper(obj, uid):
        uid = int(uid)
        user = obj.get_current_user()
        if user:
            return func(obj, uid)
        else:
            obj.write(dict(
                status=1,
                msg="please login"
            ))
            return
    return wrapper
