class parent:
    def phone(self):
        print('nokia 1100')
class child(parent):
    def phone(self):
        print('i have iphone')
c=child()
c.phone()   #the class parent is over-ridden because the child has same method within itself and please not
            #that the arg number is same.