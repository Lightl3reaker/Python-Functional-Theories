class Price():
    def payment(x=None):
        print("This is from Price class")


class another(Price):
    def payment(y=None):
        print("This is from child class")


obj = another()
obj.payment()
