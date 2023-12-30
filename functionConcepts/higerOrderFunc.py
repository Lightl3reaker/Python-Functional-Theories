def myfunc(x, fn):
    return fn(x)


value = myfunc(5, lambda y: y*2)
print(value)


def my_func(fn1, *args, **kwargs):
    return fn1(*args, **kwargs)


value1 = my_func(lambda x, y: x+y, 10, 2)
print(value1)
