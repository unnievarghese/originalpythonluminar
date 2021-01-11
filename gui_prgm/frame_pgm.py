from tkinter import *
root=Tk()
tframe=Frame()
bframe=Frame()

tframe.pack()
bframe.pack(side=BOTTOM)

btn1=Button(tframe,text='First button',fg='green')
btn2=Button(tframe,text='Second button',fg='blue')
btn3=Button(tframe,text='Third button',fg='red')
btn4=Button(bframe,text='Fourth button',fg='black')

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)

root.mainloop()