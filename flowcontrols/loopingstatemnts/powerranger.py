num=int(input("enter the number"))
result=0
digit=0
i=1
while(i<=num):
    digit = digit * 10 + num
    result+=digit
    i+=1
print(result)
