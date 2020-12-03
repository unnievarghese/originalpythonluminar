f=open("name","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip('\n')) #rstrip is used to remove \n
print(lst)