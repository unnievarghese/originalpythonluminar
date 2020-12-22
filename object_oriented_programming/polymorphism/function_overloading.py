def add():
    print('inside no arg add method')
def add(num):
    print('inside 1 arg add method')
def add(num1,num2):
    print('inside 2 arg add method')
# def without a class is funtion
#fucntion overloading is same as method overriding but without class
# same fuction but different number of arguments
print(add(1,2))   #this one works because it has two arg and add function with two parameter works because it is
                    #recently implemented
print(add(1))     #this one wont work becuase it has only 1 arg and add function with 1 parameter
                    # is not last implemented