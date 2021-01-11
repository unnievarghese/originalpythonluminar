from tkinter import *
root=Tk()
ulabel=Label(root,text="Username")
plabel=Label(root,text='Password')
uentery=Entry(root)
pentery=Entry(root)
btn=Button(root,text='Login')

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentery.grid(row=0,column=1)
pentery.grid(row=1,column=1)

#btn.grid(row=2,column=1)
btn.grid(columnspan=2)
root.mainloop()