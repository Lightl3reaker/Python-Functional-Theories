def avg(*args):
    length = len(args)
    result = 0
    for i in range(len(args)):
        pass
        result += args[i]
    if length == 0:
        return 0
    else:
        return (result/length)


x = int(input("How many numbers do you want to find average==>"))
y = []
print("Plz enter the number you want to find average!!!")
for i in range(x):
    y.append(int(input("==>")))
# print(y)
result = avg(*y)
print("Average value of {} is {}.".format(y, result))
