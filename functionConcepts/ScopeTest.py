# first example
g = 20


def myfunc(n):
    g = 10
    v = g**n
    return v


print(myfunc(2))
print("Global Variable g:", g)

# second example


def outerfunc():
    d = "green"

    def innerfunc():
        d = "python"
        print("inner:", d)
    innerfunc()
    print("outer:", d)


outerfunc()
