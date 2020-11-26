list=[120,34,675,333,1000]
list1=[]
for i in range(0,len(list)):
    list1.append(1)
c=0
for i in list:
    for j in list:
        if(i>=j):
            c+=1
    count=c
    c=0
    list1[count-1]=i
print(list1)
