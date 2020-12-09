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
        self.name=name
        self.age=age
        self.gender=gender
    def print_person(self):
        print('name:',self.name)
        print('age:', self.age)
        print('gender:', self.gender)
#reference is used to point to the class
magic=person()
magic.set_person("unnie",27,"male") #method inside class is called and use
magic.print_person() ##method inside class is called and use