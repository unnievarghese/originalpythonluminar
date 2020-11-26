list=[-1,-2,1,2,3,4]
listpos=[]
for i in list:
    if(i>=0):
        listpos.append(i)
sum1=sum(listpos)
sum2=0
for i in range(min(listpos),max(listpos)+1):
    sum2+=i
dif=abs(sum1-sum2)
if(dif!=0):
    result=dif
elif(min(listpos)==1):
    result=(max(listpos)+1)
elif(min(listpos)!=1):
    result=(min(listpos)-1)

print(result)