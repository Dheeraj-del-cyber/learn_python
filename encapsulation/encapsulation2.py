class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def show_details(self):
        print(self.__name)
        print(self.__marks)
    def update_marks(self,new_marks):
        self.new_marks=new_marks
        self.new_marks+=10
    def get_marks(self):
        print(self.new_marks)        
s1=Student("Dheeraj",98)
s1.get_marks()
s1.update_marks(98)
s1.get_marks()
