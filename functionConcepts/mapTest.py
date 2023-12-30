def factori(n):
    return 1 if n <= 1 else n*factori(n-1)


result = list(map(factori, range(1, 6)))
print("This is list format==>", result)
for i in result:
    print(i)
