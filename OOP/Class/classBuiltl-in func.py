# classes have four built-in functions
# 1.getattr(obj,name)
# 2.setattr(obj,name,value)
# 3.delattr(obj,name)
# 4.hasattr(obj,name)
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


obj = Student("Ye Yint", 103, 18)
print(getattr(obj, "name"))
print(getattr(obj, "age"))
setattr(obj, "age", 19)
print(getattr(obj, "age"))
delattr(obj, "age")#deleting attribute
print(hasattr(obj, "age"))#checking whether there is an attribute 
