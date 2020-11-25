ul=int(input("enter upper limit"))
ll=int(input("enter lower limit"))
sum=0
while(ll<=ul):
    if(ll%2!=0):
        sum+=ll
    ll+=1
print(sum)