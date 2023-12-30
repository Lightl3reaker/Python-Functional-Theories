
def square(a):
    return a**2


def cube(a):
    return a**3


def funtofun(func, n):
    return func(n)


a = int(input("Plz Enter the number you want to square:"))
b = int(input("Plz Enter the number you want to cube:"))
print("Square of {} is {}".format(a, funtofun(square, a)))
print("Cube of {} is {}".format(b, funtofun(cube, b)))
