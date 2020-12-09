#create a class of students with attribute like roll,name,course,total
#must have methods to settinh and print

class student:
    def student_data(self,roll,name,course,total):
        # self.name,self.roll1,self.course,self.total are all called instance variables
        self.name=name
        self.roll=roll
        self.course=course
        self.total=total
    def print_data(self):
        print('name:',self.name)
        print('roll:', self.roll)
        print('course:', self.course)
        print('total:', self.total)
object=student()
object.student_data(100,'ajay','bca',450)
object.print_data()