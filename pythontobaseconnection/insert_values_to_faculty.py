from originalpythonluminar.dbconnectpgm.get_connection import *

db=get_connections()
cursor=db.cursor()
sql="insert into faculty(id,name,subject)values('101','vijay','operating system')"
try:
    cursor.execute(sql)
    db.commit()
    print('qeury executed')
except Exception as e:
    print(e.args)
finally:
    db.close()