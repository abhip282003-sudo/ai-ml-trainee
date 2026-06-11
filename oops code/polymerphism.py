#Implement polymorphism using multiple classes with same method name.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def student_detail(self):
        print("name is:",self.name)
        print("age is :",self.age)
        
class Student2:
    def __init__(self,gender,grade):
        self.gender=gender
        self.grade=grade
    def student_detail(self):
        print("gender is ",self.gender)
        print("grade is:",self.grade)
    
s1=Student("Abhishek",33)
s2=Student2("male","A")
for obj in [s1, s2]:
    obj.student_detail()
    