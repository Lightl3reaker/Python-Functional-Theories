from functools import lru_cache


@lru_cache(maxsize=None)
def fibo(n):
    return 1 if n < 3 else fibo(n-1)+fibo(n-2)


x = int(input("Plz Enter a Nunber:"))
print(fibo(x))
