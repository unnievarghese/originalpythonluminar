list=[7,2,3,6,8,1,10]
element=int(input("enter the element to search:"))
for i in range(0,len(list)):
    for j in range(0,len(list)):
        if list[j]>=list[i]:
            temp=list[j]
            list[j]=list[i]
            list[i]=temp
low = 0
upp = len(list) - 1
flag=0
for i in range(0,len(list)//2):
    mid = list[(upp + low) // 2]
    if (element==mid):
        flag=1
        break
    elif (element>mid):
        low=list.index(mid)+1
    elif (element<mid):
        upp=list.index(mid)-1
if flag==1:
    print("number found")
else:
    print('number not found')