#list is defined by [] or by list()
#list preserves order of insertion
#duplicates are allowed

list=['java','python','python','java','c#','javascript']
print(list)
print(list[0])
print(list[-1])
print(list[-2])
print(list[-4:-1])
print(list[0:4:2])
for x in list:
    print(x)
#adding new element
list.append("dark")
print(list)
#replacing java with ruby
list[0]='ruby'
print(list)
#inserting without loosing elements
list.insert(3,'php')
print (list)