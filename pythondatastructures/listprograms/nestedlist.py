list=[[1001,'ajay','mca',150],
      [1002,'vijay','bca',145],
      [1003,'arun','mca',150],
      [1004,'amal','bca',135]]
#print students name
for students in list:
    print(students[1])
#print roll number
for students in list:
    print(students[0])
#print students details with course mca
for students in list:
    if students[2]=='mca':
        print(students)
#print students details with total greater than 140
for student in list:
    if student[3]>140:
        print(student)
#print sum of students total and group by course
summca=0
sumbca=0
for student in list:
    if student[2]=='mca':
        summca+=student[3]
    elif student[2]=='bca':
        sumbca+=student[3]
print('sum of mca:',summca,',','sum of bca:',sumbca)