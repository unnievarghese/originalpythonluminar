list=[2,5,6,3]
listn=[]
sum=0
for i in list:
    for j in list:
        if(j!=i):
            sum+=j
    listn.append(sum)
    sum=0
print(listn)
