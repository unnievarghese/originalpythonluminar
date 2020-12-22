class Employee:
    def __init__(self,id,name,designation,sallary,exp):
        self.id=id
        self.name=name
        self.designation=designation
        self.sallary=sallary
        self.exp=exp

ajay=Employee(100,'ajay','developer',25000,3)           #creating objects
vijay=Employee(101,'vijay','qa',20000,2)
arun=Employee(102,'arun','accounts',15000,1)
nithya=Employee(103,'nithya','pro',30000,4)
sreedevi=Employee(104,'sreedevi','developer',25000,3)

lst=[]
lst.append(ajay)
lst.append(vijay)
lst.append(arun)
lst.append(nithya)
lst.append(sreedevi)
print(list(map(lambda x:x.name.upper(),lst)))