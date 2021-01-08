#> import mysql
#> establis connection
#> cursor object
#> execute queries
#> close database

import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password@123'
)
cursor =db.cursor()
sql='SELECT VERSION()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)