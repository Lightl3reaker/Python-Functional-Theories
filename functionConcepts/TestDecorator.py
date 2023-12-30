def myfun(x, y):
    print(int(x/y))


myfun(10, 5)


def working(fn):
    def inner(x, y):
        if x < y:
            x, y = y, x
        return fn(x, y)
    return inner


result = working(myfun)
result(5, 20)
