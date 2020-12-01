list=[[1001,'ajay','qa',1981,2003],
      [1002,'vijay','developer',1992,2008],
      [1003,'arun','ba',1989,2010],
      [1004,'amal','developer',2009,2010],
      [1004,'vimal','developer',1987,1989]]
#print all employee designation
#print employee whose designation in develooper
#print all employee who worked in 80's
#print all employee details with exp>9
list_developer=[]
list_80=[]
list_exp=[]
for employee in list:
    print(employee[1]+':'+employee[2])
    if employee[2]=='developer':
        list_developer.append(employee[1])
    if employee[4]<1990:
        list_80.append(employee[1])
    if employee[4]-employee[3]>9:
        list_exp.append(employee[1])
print('developers list:',list_developer,'\n','employess of 80s:',list_80,'\n','employes with 9 yrs exp:',list_exp)