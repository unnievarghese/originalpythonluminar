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

print("the least positve element is: ",result)

print("===============<another method>=========================")
cnt=1
for j in range(0,len(list)):
    if cnt in list:
        cnt+=1
    else:
        print("the least positve element is: ",cnt)
        break
