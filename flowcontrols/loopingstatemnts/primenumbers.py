num=int(input("enter the number to check"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
if(flag==0):
    print("the number %i is prime"%num)
else:
    print("the number %i is not prime"%num)