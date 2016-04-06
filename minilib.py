from functools import wraps
from flask import session


def get_current_user_role():
    "none" if not session.get('userlevel',None) else\
        session['userlevel']


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return "Neautorizovany pristup"
            return f(*args, **kwargs)

        return wrapped

    return wrapper
