list=[1,2,3,4,6,7]

for i in list:
    for j in range(list[-3:]):
        if (i!=j) and i+j==6:
            print(i,j)

print(list[1])