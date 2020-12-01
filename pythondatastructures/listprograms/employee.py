list=[[1001,'ajay','qa',15000],
      [1002,'vijay','developer',25000],
      [1003,'arun','ba',15000],
      [1004,'amal','developer',30000]]
totalsallary=0
count=0
qa_sallary=0
ba_sallary=0
developer_sallary=0
for employee in list:
    print(employee[0])
    totalsallary+=employee[3]
    if employee[2]=="developer":
        developer_sallary+=employee[3]
        count+=1
    if employee[2]=='qa':
        qa_sallary+=employee[3]
    if employee[2]=='ba':
        ba_sallary+=employee[3]
print("total sallary:",totalsallary,'\n','no.of developer:',count,'\n','sallary by group:','\n','qa_sallar:'
      ,qa_sallary,'\n','ba_sallary:',ba_sallary,'\n','developer_sallary:',developer_sallary)