def Gen():
    data = 10
    yield data
    yield data+1
    yield data+2


result = Gen()
for i in result:
    print(i)
