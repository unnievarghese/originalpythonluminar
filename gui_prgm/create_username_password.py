from tkinter import *
from tkinter import messagebox
from originalpythonluminar.dbconnectpgm.get_connection import get_connections
flag=1
def update_table():
    name=ne.get()
    username=ue.get()
    password=pe.get()
    db=get_connections()
    cursor=db.cursor()
    try:
        cursor.execute('select id from users order by id desc limit 1;')
        id=int(cursor.fetchone()[0])+1
        cursor.execute('insert into users (id,name,username,password)values(%s,%s,%s,%s)',
        (id,name,username,password))
        db.commit()
    except Exception as e:
        print(e.args)
        messagebox.showerror('Account not created')

root=Tk()
nl=Label(root,text='Enter Name')
ul=Label(root,text='Enter New username')
pl=Label(root,text='Enter New Password')
ne=Entry(root)
ue=Entry(root)
pe=Entry(root)
btn=Button(root,text='Create Account',command=update_table)

nl.grid(row=0,column=0)
ul.grid(row=1,column=0)
pl.grid(row=2,column=0)
ne.grid(row=0,column=1)
ue.grid(row=1,column=1)
pe.grid(row=2,column=1)
btn.grid(row=3,column=1)
root.mainloop()