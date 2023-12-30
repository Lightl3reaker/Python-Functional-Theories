def mySum(x1, y1):
    return x1+y1


def myReduceFunc(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first


list = [1, 2, 3, 4, 5, 6, 7]
print(myReduceFunc(mySum, list))
