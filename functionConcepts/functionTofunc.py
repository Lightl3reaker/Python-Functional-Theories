def square(a):
    return a**2


def cube(a):
    return a**3


def num(number):
    if number == 1:
        return square
    else:
        return cube


sq = num(1)
cu = num(2)
x = int(input("Plz enter the number you want to square:"))
y = int(input("Plz enter the number you want to cube:"))
print("The square of {} is {}".format(x, sq(x)))
print("The cube of {} is {}".format(y, cu(y)))
