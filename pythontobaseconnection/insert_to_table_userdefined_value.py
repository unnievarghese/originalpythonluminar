from originalpythonluminar.dbconnectpgm.get_connection import *
db=get_connections()
cursor=db.cursor()
n=int(input('Enter number of rows to insert:'))
for i in  range(n):
    values=input().split()
    sql='insert into faculty(id,name,subject)values(%s,%s,%s)'
    try:
        cursor.execute(sql,values)
        db.commit()
        print('insertion success')
    except Exception as e:
        print(e.args)