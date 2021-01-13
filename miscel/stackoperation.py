size=int(input('enter the size of stack'))
stk=[]
option=1
indx=0
def push(element):
    global indx
    if indx==size:
        print('stack is full')
    else:
        indx+=1
        stk.append(element)
def pop():
    global indx
    if indx==0:
        print('stack is empty')
    else:
        indx-=1
        stk.pop()
def display():
    print(stk)
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