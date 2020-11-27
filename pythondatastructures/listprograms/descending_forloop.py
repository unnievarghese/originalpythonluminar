list=[120,34,120,675,333,120,333,1000,333]
for i in range (0,len(list)):
    for j in range (0,len(list)):
        if(list[j]<=list[i]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

print(list)