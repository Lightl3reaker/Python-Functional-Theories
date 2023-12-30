def logger(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{} :called {} :recent data:{}'.format(dt, fn.__name__, result))
        return result
    return inner


@logger
def myfun1(x, y):
    """From function 1"""
    return x+y


@logger
def myfun2():
    """From function 2"""
    return 10


myfun1(10, 20)
myfun2()
