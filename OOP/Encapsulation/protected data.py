class Parent:
    def __init__(self, age):
        self._age = age


class Sub(Parent):
    def getData(self):
        print(self._age)


obj = Sub(100)
obj.getData()
