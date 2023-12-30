# first example
g = 20


def myfunc(n):
    global g
    v = g**n
    return v


print(myfunc(2))
print("Global g:", g)
