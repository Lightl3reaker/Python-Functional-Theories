def myFunc(x, y, z):
    print(x, y, z)


def pFunc(yy, zz):
    return myFunc(10, yy, zz)


pFunc(100, 200)
