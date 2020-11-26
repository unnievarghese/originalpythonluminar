marklist=[]
mark=1
while(mark>=0):
    mark=int(input("enter the mark:"))
    marklist.append(mark)
marklist.remove(-1)
print(marklist)
marklist.insert(3,24)
print(marklist)
marklist[2]=100
print(marklist)
