employee={101:{'id':101,'name':'ajay','designation':'qa','sallary':15000},
          102:{'id':102,'name':'vijay','designation':'developer','sallary':15000},
          103:{'id':103,'name':'sumesh','designation':'coustomer care','sallary':15000},
          104:{'id':104,'name':'virat','designation':'developer','sallary':15000},
          105:{'id':105,'name':'vinod','designation':'accountant','sallary':15000}}

def Print(**arg):
    id=arg.get('id')
    employee_details=arg.get('property')
    if id in employee:
        if employee_details in employee[id]:
            print(employee[id][employee_details])
        else:
            print('for employee',id,'employee details not found')
    else:
        print('employee not found')
a=int(input())
b=input()
Print(id=a,property=b)