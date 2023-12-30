class Base1:
    def multi(self, a, b):
        return a*b


class Base2(Base1):
    def add(self, a, b):
        return(a+b)


class Base3(Base2):
    def sub(self, a, b):
        return a-b


obj = Base3()
print("This is from base1", obj.multi(5,3))
print("This is from base2", obj.add(5,3))
print("This is from base3", obj.sub(5,3))
