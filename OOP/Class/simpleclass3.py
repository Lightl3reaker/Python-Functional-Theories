class Myclass:
    def __init__(self):
        self.name = "Ye Yint"
        self.age = 18
        self.hobby = "Maths"
        print(self.name, " ", self.age, " ", self.hobby)

    def update(self):
        self.name = "LightBreaker"
        self.age = 19
        self.hobby = "Programming"
        print(self.name, self.age, self.hobby)


print("Before update==>", end="")
obj = Myclass()
print("Manual Update==>", end="")
obj.name = "Lucifer"
obj.age = 19
obj.hobby = "research"
print(obj.name, " ", obj.age, " ", obj.hobby)
print("Auto-Update==>", end=" ")
obj.update()

