def myfun(n):
    def adding(data):
        return data+n
    return adding


add10 = myfun(10)
add20 = myfun(20)
print(add10.__closure__)
print(add10.__closure__[0].cell_contents)
