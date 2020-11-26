list=[120,11,12,13,14]
element=int(input("enter the element to search:"))
for i in list:
    if element==i:
        print("The elment is present in the list.")
        break
print("The index value is:",end="")
for i in list:
    if element==i:
        print(list.index(i),end=" ")