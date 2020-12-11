#class
#plan,desing pattern,template,blueprint


#object
# real world entity

#refrence?
#used to perform operations on object

# class keyord is used to create class

class person:  #we created class named person
    # NOW TO SET a PERSONS attritube as self.name,self.age,self.gender
    # def declared within class is called method
    def set_person(self,name,age,gender):  #
        self.name=name    # lines from 17 to 19 are caled instance varibles
        self.age=age
        self.gender=gender
    def print_person(self):
        print('name:',self.name)  #to access instance variable inside class use slef key
        print('age:', self.age)
        print('gender:', self.gender)
#reference is used to point to the class
magic=person()
magic.set_person("unnie",27,"male") #method inside class is called and use
magic.print_person() #method inside class is called and used
#to access variables outside class
print(magic.name)
# static varibles or class level variables
# static is used for efficient memory usage
#it is accessed inside class using class name.

# it can be said that there are 2 types of varibles 1)intance 2)static

# different types of methods: 1)static method 2)instance method 3) class method
#instance methods are the ones commolny used which has a self keyword inside braces
#for declaring static method dont have to use self keyword but a decorator called @staticmethod is used a
#line above declaring the static method
# decorator for class method is @classmethod and it is used to manipulate class level variables