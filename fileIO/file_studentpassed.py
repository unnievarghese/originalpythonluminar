f=open('student_list','r')
set_total=set()
for student in f:
    set_total.add(student.rstrip('\n'))
f=open('student_passed','r')
set_failed=set()
for student in f:
    set_failed.add(student.rstrip('\n'))
print(set_total-set_failed)