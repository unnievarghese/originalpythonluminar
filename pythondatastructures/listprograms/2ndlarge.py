list=[120,11,65,4,32,65,7]
c=0
for i in list:
    for j in list:
        if(i>=j):
            c+=1
    count=c
    c=0
    if count==len(list)-1:
        print("The second largest value is:",i)

