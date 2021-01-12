from tkinter import *
root=Tk()
ulabel=Label(root,text='Username')
plabel=Label(root,text='password')
uentry=Entry(root)
pentry=Entry(root)
btn=Button(root,text='Login')

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)
uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(row=2,column=1)
root.mainloop()