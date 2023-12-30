from functools import wraps


def log(fn):
    @wraps(fn)
    def with_log(*args, **kwargs):
        print(fn.__name__+" was called")
        return fn(*args, **kwargs)
    return with_log


@log
def myfun(x):
    """Some operation just like arithmetic"""
    return x+x+x


myfun(5)
print(myfun.__name__)
print(myfun.__doc__)
