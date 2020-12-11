class Parent():
    def m1(self):
        print('inside parent')
class child():
    def m2(self):
        print('inside child')
class subchild(child,Parent):
    def m3(self):
        print('inside subchild')

sc=subchild() #this class can call all methods within itself and the clases child,parent
sc.m3()
sc.m2()
sc.m1()
print()
# other classes can only call the methods within itself