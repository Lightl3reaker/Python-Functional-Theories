from abc import ABC, abstractmethod


class Price():
    def print_slip(self, amount):
        print("Payment amount:", amount)

    @abstractmethod
    def payment(self):
        print("This is from abstact class")


class creditcard(Price):
    def payment(self, amount):
        print("Payment form credit card:", amount)


class mobilebanking(Price):
    def payment(self):
        return super().payment()


obj = creditcard()
obj.print_slip(1000)
obj.payment(2000)
obj1 = mobilebanking()
obj1.payment()
