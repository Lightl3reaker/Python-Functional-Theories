class Price:
    def payment(self, dataType, *args):
        if dataType == "int":
            data = 0
            count = 0
            for i in args:
                data += i
                count += 1
            print(data)
            print("There are {} parameters called.".format(count))
        elif dataType == "str":
            data = ''
            count = 0
            for i in args:
                data += i
                count = 1
            print(data)
            print("String data type is called.")


obj = Price()
obj.payment("int", 5, 5, 6)
obj.payment("str", "Mya", " ", "maung")
