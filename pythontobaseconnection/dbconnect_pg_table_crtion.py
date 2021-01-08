from originalpythonluminar.dbconnectpgm.get_connection import *

db=get_connections()
cursor=db.cursor()
sql='create table faculty(id varchar(50),name varchar(10),subject varchar(50))'
try:
    cursor.execute(sql)
    print('success')
except Exception as e:
    print(e.args)
finally:
    db.close()