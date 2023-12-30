class Price:
    def payment(self, x=None, y=None):
        if x != None and y != None:
            return x*y
        if x != None:
            return x*x
        else:
            return None


obj = Price()
print("With no arg:", obj.payment())
print("With one arg:", obj.payment(10))
print("With two args:", obj.payment(10, 2))
