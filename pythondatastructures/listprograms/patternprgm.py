list=[6,6,8,9,4,2,3]
outputlist=[]
for i in list:
    if(i>5):
        outputlist.append(i+1)
    else:
        outputlist.append(i - 1)
print(outputlist)