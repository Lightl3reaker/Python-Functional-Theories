from functools import reduce
import operator

list1 = [1, 2, 3, 4, 5, 6]
list2 = []#emptylist
list3 = [False, 0, 1]
output1 = reduce(lambda x, y: x*y, list1)#reduce() run the process till provided list end 
output2 = reduce(operator.mul, list1)
print(output1)
print(output2)
output3 = operator.lt(10, 20)#less than
output4 = operator.gt(10, 20)#Greater than
print(output3)
print(output4)
output5 = operator.is_("a", "b")#operator.is_ checks whether two provided variables are equal or not
output6 = operator.is_not("a", "b")
print(output5)
print(output6)
print(operator.truth(list1))
print(operator.truth(list2))
print(operator.truth(list3))
