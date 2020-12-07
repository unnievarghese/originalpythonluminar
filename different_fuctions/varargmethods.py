#for passing unlimted number of argumnets
#the arguments will be passed as tuple
def add(*num):
    sum=0
    for i in num:
       sum+=i
    print(sum)
add(1,2,3,4)
add(5,6,7,8)
add(34,2,34)

# for passing a an argument as a dcitionary,usefull for mentioning the importance of the dict value
def func(**arg):
    print(arg)
func(name='unnie',place='kochi',age=17)