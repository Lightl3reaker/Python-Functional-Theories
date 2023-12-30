# error coding
def bookshop(name, quantity, unit, blist=[]):
    blist.append("{} {} {}".format(name, quantity, unit))
    return blist


store1 = bookshop("java", 1, "book")
bookshop("python", 2, "book")
# this will add to previous list instead of creating a new list
store2 = bookshop("c++", 3, "book")
print(store1)
print(store2)
# solution
print("\nThis is solution")


def bshop(name, quantity, unit, blist=None):
    if not blist:
        blist = []
    blist.append("{} {} {}".format(name, quantity, unit))
    return blist


space1 = bshop("Golang", 1, "book")
bshop("Kotlin", 2, "book", space1)
space2 = bshop("C#", 3, "book")
print(space1)
print(space2)
