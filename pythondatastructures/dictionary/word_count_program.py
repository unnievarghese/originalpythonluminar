text="hello hai hai hello hai"
words=text.split()
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
# another longer way of doing it:
text="hello hai hai hello hai"
list=text.split()
count=0
set1=set(list)
for letter in set1:
    for listmember in list:
        if letter==listmember:
            count+=1
    print(letter,count)
    count=0