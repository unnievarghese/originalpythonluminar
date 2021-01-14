size=int(input('enter the size of stack'))
stk=[]
option=1
top=0
def push(element):
    global top
    if top>=size:
        print('stack is full')
    else:
        stk.insert(top, element)
        top+=1
def pop():
    global top
    if top==0:
        print('stack is empty')
    else:
        print(stk[top - 1], 'popped')
        top -= 1
def display():
    print(stk[:top])
while(option!=0):
    option=int(input(('enter operaiton u want to perfrom 1)push 2)pop 3)display')))
    if option==1:
        element=input()
        push(element)
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        if option!=0:
            print('invalid option')