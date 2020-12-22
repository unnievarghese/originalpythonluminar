lst=[1,2,3,4,5,6]
print(list(map(lambda num:num**2,lst)))
print(list(map(lambda num:num**3,lst)))

#print the names in uppercase
names=['ajy','vijay','anu','raji','ragu']
print(list(map(lambda name:name.upper(),names)))

#to print names starting with a
print(list(filter(lambda name:name[0]=='a',names)))