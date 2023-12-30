class Myclass:
    def myMethod(self):
        self.x = 5
        self.y = 10


obj1 = Myclass()
obj2 = Myclass()
obj1.myMethod()
obj2.myMethod()
print(obj1.x, obj1.y)
