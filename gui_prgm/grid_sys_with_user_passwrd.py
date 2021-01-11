from tkinter import *
from tkinter import messagebox
root=Tk()
from originalpythonluminar.dbconnectpgm.get_connection import get_connections
def db_connect(username,passwrod):
    print('inside')
    db=get_connections()
    cursor=db.cursor()
    try:
        cursor.execute('select * from users where username=%s and password=%s',(username,passwrod))
        user=cursor.fetchone()
        return user
    except EXCEPTION as e:
        print(e.args)

def athenticate_user():
    uname=uentery.get()
    upwd=pentery.get()
    user=db_connect(uname,upwd)
    if user==None:
        messagebox.showerror('Invalid user','Error')
    else:
        messagebox.showinfo('User succecfully logged','Information')


ulabel=Label(root,text="Username")
plabel=Label(root,text='Password')
uentery=Entry(root)
pentery=Entry(root)
btn=Button(root,text='Login',command=athenticate_user)

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentery.grid(row=0,column=1)
pentery.grid(row=1,column=1)

#btn.grid(row=2,column=1)
btn.grid(columnspan=2)
root.mainloop()