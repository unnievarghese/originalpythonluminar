from originalpythonluminar.dbconnectpgm.get_connection import *

db=get_connections()
cursor=db.cursor()
query='select * from faculty'
try:
    cursor.execute(query)
    queryset=cursor.fetchall()
    for faculty in queryset:
        print(faculty)
except Exception as e:
    print(e.args)
finally:
    db.close()