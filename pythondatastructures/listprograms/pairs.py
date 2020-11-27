list=[1,2,3,4,6,7,0,3,5]
l=1
k=1
for i in list:
    for j in range(k,len(list)):
        if  i+list[j]==6:
            print(i,list[j])
    k+=1