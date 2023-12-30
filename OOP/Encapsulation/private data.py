# we use two underscore in private variables
class Parent:
    def __init__(self, age):
        self.__age = age


class Child(Parent):
    def data(self, input):
        self.__age = input
        return self.__age

    def get_data(self):
        print(self.__age)


obj = Child(10)
print("Before modifing", obj.__dict__)
print("After modifing",end=" ")
obj.data(20)
obj.get_data()
print("THIS IS ERROR==>",end=" ")
p=Parent(30)
print(p.__age)
