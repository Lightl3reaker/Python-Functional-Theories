# closure function
def myfun(n):
    def adding(data):
        return data+n
    return adding


add10 = myfun(10)
add20 = myfun(20)
print("This will be add10==>", add10(2))
print("This will be add20==>", add20(3))
print("This is combination fo add10 and add20==>", add20(add10(4)))
