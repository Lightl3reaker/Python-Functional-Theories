# keyword arguments return in dictionary form
def my_func(a, b, *, c, **kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs)


my_func(10, 20, k=30, c=40)


def other(**key):
    print(key)


other(a=100, b=200, c=300)
