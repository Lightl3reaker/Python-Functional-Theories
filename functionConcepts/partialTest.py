import functools
from functools import partial


def myFunc(x, y, z):
    print(x, y, z)


output = partial(myFunc, 10)
output(20, 30)
