#inheritacne
#using names
# parent      based         super
#         or           or
# child       derived        subclass

class Parent:
    def mobile(self):
        print('ihave mobie')
class child(Parent): #here the child class invokes the methods of the parent class
    def bike(self):   #the child class can also have other methods.
        print('i have bike')

obj=child()
obj.mobile()
obj.bike()
