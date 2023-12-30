#from typing import Iterator


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]


def check_Even(number):
    if number % 2 == 0:
        return True
    else:
        return False


even_numbers_iterator = filter(check_Even, numbers)
even_numbers = list(even_numbers_iterator)
print(even_numbers)
