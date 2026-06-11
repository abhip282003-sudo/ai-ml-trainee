#Implement single inheritance using Person and Student classes
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display_details(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no
    def student_detail(self):
        self.display_details()
        print("roll_no",self.roll_no)
        


std=Student("abhishek",34,86)
std.student_detail()