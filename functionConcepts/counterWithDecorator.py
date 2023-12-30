def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {0} was called {1}".format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner


def add(a, b=0):
    """adding two values using decorator"""
    print(int(a+b))


def sub(a, b=0):
    """substracting two values using decorator"""
    print(int(a-b))


result1 = counter(add)
result2 = counter(sub)
result1(5, 4)
result2(10, 6)
