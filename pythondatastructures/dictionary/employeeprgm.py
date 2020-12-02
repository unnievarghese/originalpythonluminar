employee={101:{'id':101,'name':'ajay','designation':'qa','sallary':15000},
          102:{'id':102,'name':'vijay','designation':'developer','sallary':15000},
          103:{'id':103,'name':'sumesh','designation':'coustomer care','sallary':15000},
          104:{'id':104,'name':'virat','designation':'developer','sallary':15000},
          105:{'id':105,'name':'vinod','designation':'accountant','sallary':15000},
}
print('----------------------')
print('print empoyee name:')
print('----------------------')
for key in employee:
    print(employee[key]['name'])
print('---------------------------------------------------')
print('check if experince is given if not add experince')
print('---------------------------------------------------')
for key in employee:
    if 'experience' not in employee[key]:
        employee[101]['experience']=5
        employee[102]['experience'] =3
        employee[103]['experience'] =3
        employee[104]['experience'] = 1
        employee[105]['experience'] =7
print(employee)
print('----------------------')
print('add 5000 to sallary')
print('----------------------')
for key in employee:
    employee[key]['sallary']+=5000
print(employee)
print('-----------------------------')
print('print all key value pairs:')
print('-----------------------------')
for key in employee:
    print(key,employee[key])
    for key2 in employee[key]:
        print(key2,employee[key][key2])