def x(y, z): return y**z


print(x(2, 3))

a = lambda b, *args, c, **kwargs: (b, args, c, kwargs)
print(a(10, "h", "e", "l", "l", "o", c=20, d=1, e=2, f=3))
