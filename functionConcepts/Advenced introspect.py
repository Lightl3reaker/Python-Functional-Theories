import inspect
import math
from math import sin
from inspect import isfunction, ismethod


def myfun(x, y, z=10, *, kw1, kw2=2):
    return x+y


print("This is function name==>", myfun.__name__)  # This is comment
print("This is positional args==>", myfun.__defaults__)
print("This is keyword args==>", myfun.__kwdefaults__)
print("This is variables==>", myfun.__code__.co_varnames)
print("This is the number of positional args==>", myfun.__code__.co_argcount)
print(inspect.getcomments(myfun))
print(inspect.getsource(myfun))
print(inspect.isfunction(myfun))
print(inspect.ismethod(myfun))
print(inspect.getmodule(sin))
