# use "issubclass(class1,class2)" to know if class1 is a subclass of class2
# use "isinstace(obj,class1)" to know if obj is the object(instance) of class1
class Parent:
    pass


class Child(Parent):
    pass


print("Child is the subclass of Parent:", issubclass(Child, Parent))
obj = Child()
print("obj is the object of Child class:", isinstance(obj, Child))
print("obj is the object of Parent class:", isinstance(obj, Parent))
