from functools import *
lst=[1,2,3,4,5,6]
print(reduce(lambda num1,num2:num1+num2,lst))
print(reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)) #max
print(reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)) #min
#sum on even num
print(reduce(lambda num1,num2:num1+num2,list(filter(lambda num:num%2==0,lst))))
#max of even
print(reduce(lambda  num1,num2:num1 if num1>num2 else num2,list(filter(lambda num:num%2==0,lst))))
#min of even
print(reduce(lambda  num1,num2:num1 if num1<num2 else num2,list(filter(lambda num:num%2==0,lst))))