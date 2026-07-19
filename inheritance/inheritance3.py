class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course 
    def display(self):
        print("Branch",self.course)        
    def study(self):
        print("studying python")     
s1=Student("Dheeraj",19,"ISE")
s1.show()
s1.display()
s1.study()
