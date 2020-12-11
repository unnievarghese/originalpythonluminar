class Parent():
    def m1(self):
        print('inside parent')
class child(Parent):
    def m2(self):
        print('inside child')
class subchild(child):
    def m3(self):
        print('inside subchild')
sc=subchild() #this class can call all methods within itself and the clases child,parent
sc.m3()
sc.m2()
sc.m1()
print()
ch=child()   #this class can call all methods within itself and the class parent
ch.m2()
ch.m1()
print()
p=Parent()   #this clas  can call only methods from itself
p.m1()