size=int(input('Enter the size of queue:'))
q=[]
front=0
rear=0
option=1
def insert(element):
    global rear
    if rear<size:
        q.insert(rear,element)
        print('Inseriton of',q[rear],'complete')
        rear+=1
    else:
        print("queue full\n")
def delete():
    global front
    if front<rear:
        print(q[front],'Popped')
        front+=1
    else:
        print('queue empty\n')
def display():
    for i in q[front:rear]:
        print(i)

while(option!=0):
    option=int(input('choose the operation to perform\n1) Insertion\t2)Deletion\n3)Dispay'))
    if option==1:
        element=input()
        insert(element)
    elif option==2:
        delete()
    elif option==3:
        display()
    else:
        if option!=0:
            print('Invalid option')