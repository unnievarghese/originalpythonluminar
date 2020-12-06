f=open('student_list','r')
f1=open('student_passed','r')
def convert_to_set(file):
    file_set=set()
    for names in file:
        file_set.add(names.rstrip('\n'))
    return file_set
student_set=convert_to_set(f)
student_passed=convert_to_set(f1)
print(student_set-student_passed)