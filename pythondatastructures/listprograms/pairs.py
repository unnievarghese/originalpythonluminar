list=[1,2,3,4,6,7]
for i in list:
    for j in range(i,list[-1]):
        if (i!=j) and i+j==6:
            print(i,j)

