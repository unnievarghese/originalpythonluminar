class maths:
    def add(self):
        print('inside no arg add method')
    def add(self,num):
        print('inside 1 arg add method')
    def add(self,num1,num2):
        print('inside 2 arg add method')
# same method but different number of arguments
m=maths()
print(m.add(1,2))   #this one works because it has two arg and add method with two parameter works because it is
                    #recently implemented
print(m.add(1))     #this one wont work becuase it has only 1 arg and add method with 1 parameter
                    # is not last implemented