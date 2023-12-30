x=3
y=5
def myfunc(a:'Some value from function call')->"multiply"+str(max(x,y))+"times":
    """This is DocString."""
    return a*(max(x,y))
data=myfunc(2)
print(data)
print(myfunc.__doc__)#for docstring
print(myfunc.__annotations__)#for parameter
    