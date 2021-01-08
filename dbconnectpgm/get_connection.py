import mysql.connector
def get_connections():
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        database='cms',
        password='Password@123'
    )
    return db