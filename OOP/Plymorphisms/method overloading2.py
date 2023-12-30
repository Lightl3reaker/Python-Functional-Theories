class Price:
    def payment(self, *args):
        data = 0
        count = 0
        for i in args:
            count += 1
            data += i
        print(data)
        print("There are {} parameters passed".format(count))


obj = Price()
obj.payment(5,5,4)
obj.payment(3,4,5,7,1,2)
