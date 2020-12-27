#higgehst sallary
from functools import *
class Employee:
    def __init__(self,id,name,designation,sallary,exp):
        self.id=id
        self.name=name
        self.designation=designation
        self.sallary=sallary
        self.exp=exp
    def __str__(self):
        return self.name

f=open('employee')
employee=[]
for lines in f:
    id,name,designation,sallary,exp=lines.rstrip('\n').split(',')
    employee.append(Employee(id,name,designation,sallary,exp))
h_sallary=(reduce(lambda sallary1,sallary2:sallary1 if sallary1>sallary2 else sallary2,
             list(map(lambda x:x.sallary,employee)) ))
#highest sallreid emplyee
employee1=(list(filter(lambda x:x.sallary==h_sallary,employee)))
for i in employee1:
    print(i)

#highest sallary of developers
sallary_devep=reduce(lambda sallary1,sallary2:sallary1 if sallary1>sallary2 else sallary2,
                     list(map(lambda x:x.sallary,list(filter(lambda x:x.designation=='developer',employee)))))
print(sallary_devep)