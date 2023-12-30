# There are five class built-in attributes
# 1.__dict__
# 2.__doc__
# 3.__name__
# 4.__module__
# 5.__bases__
class Myclass:
    var = "Programming"

    def active():
        print(f"Hello from {Myclass.var}")


print(Myclass.__dict__)
