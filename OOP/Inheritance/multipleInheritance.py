# multiple inheritance
class Parent:
    def parent(self):
        print("This is from parent")


class Relative:
    def relative(self):
        print("This is from relative")


class Child(Parent, Relative):
    def child(self):
        print("this is from child")


obj = Child()
obj.parent()
obj.relative()
obj.child()
