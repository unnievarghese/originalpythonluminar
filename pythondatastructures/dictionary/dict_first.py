students={"roll":100,"name":'ajay','course':'bca'}
print(students['name']) #print name
print(students['course'])#print course
for item in students:    # wen iterating only the key form dictionary is passed to the variable
    print(students[item])
# another method to iterate key and value
for k,v in students.items():
    print(k,v)
#updating in item
students['name']='AJAY'
print(students)
# from all the above it is clear that inserion order in preserved
#if keyvalue pair is not avalable add it
if 'total' not in students:
    students['total']=150
print(students)
#add 50 to total
students['total']=students['total']+50
print(students)
students={100:{"roll":100,"name":'ajay','course':'bca'},
           101:{"roll":100,"name":'ajay','course':'bca'},
          }
print(students[100]['name'])