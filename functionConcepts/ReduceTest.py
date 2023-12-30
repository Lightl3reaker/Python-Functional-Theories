import functools
list = [1, 2, 3, 4, 5, 6, 7]
print("The sum of all elements from list:", end="")
print((functools.reduce(lambda a, b: a+b, list)))
print("Greatest Integer in the list:", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list))
print("Smallest Integer in the list:", end="")
print(functools.reduce(lambda a, b: a if a < b else b, list))
