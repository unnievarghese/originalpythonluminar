f=open('cyclone')
dict={}
for line in f:
    words=line.rstrip('\n').split()
    for word in words:
        word=word.rstrip(',')
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)
high=max(dict,key=dict.get)
print(high,dict[high])