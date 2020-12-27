first=[1,2,3,4,6,7]
second=[4,5,6]
# for i in first:
#     for j in second:
#         print((i,j),end=' ')
#using list cmprehesnion:
pairs=[(i,j) for i in first for j in second]
print(pairs)
#finding squares
print([i**2 for i in first])

# num<5=num-1
# num>5=num+1
data=[i+1 if i>5 else i-1 for i in first]
print(data)