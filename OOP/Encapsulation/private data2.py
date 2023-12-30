class animal:
    def __init__(self, name, color, age, behavior):
        self.__color = color
        self.__name = name
        self.__age = age
        self.__behavior = behavior


class dog(animal):
    def dmodify(self, name, color, age, behavior):
        self.__color = color
        self.__name = name
        self.__age = age
        self.__behavior = behavior

    def dget_data(self):
        print(self.__name, self.__age, self.__color, self.__behavior)


obj = dog("mimi", "yellow", 3, "eat")
print("Before modifing==>",obj.__dict__)
obj.dmodify("aung net", "black", 5, "bark")
obj.dget_data()
