def fact(num):
    res=1
    while(num>0):
        res*=num
        num-=1
    return res
print(fact(5))
