def myDec_1(fn):
    def inner():
        print("running decorator1")
        return fn()
    return inner


def myDec_2(fn):
    def inner():
        print("running decorator2")
        return fn()
    return inner


@myDec_1
@myDec_2
def myfun():
    print("running myfun")


myfun()
