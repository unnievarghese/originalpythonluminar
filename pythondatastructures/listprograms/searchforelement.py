list=[120,11,12,13,12,14,12,12,12]
flag=0
element=int(input("enter the element to search:"))
for i in list:
    if element==i:
        flag+=1
        break
    else:
        flag=0
if flag!=0:
    print("The elment is present in the list.")
    print("The index values are:", end="")
    for i in range(len(list)):
        if element == list[i]:
            print(i, end=" ")
else:
    print("element not found")
