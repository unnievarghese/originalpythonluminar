num=int(input("enter the num"))
res=0
while(num!=0):
    digit=num%10
    res+=digit**3
    num= num//10
print(res)