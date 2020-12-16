import random
list1=[]
dict={}
sorted_dict={}
while len(dict)<5:
    dict[(random.randint(0,9))]=1
for i in dict:
    list1.append(i)
for i in range(-1,len(list1)-1):
    dict[list1[i+1]]=2*(list1[i])
print('sample output before sorting:')
print(dict)
print('sample output after sorting:')
list2=sorted(dict,key=dict.get)
for i in list2:
    if i not in sorted_dict:
        sorted_dict[i]=dict[i]
print(sorted_dict)