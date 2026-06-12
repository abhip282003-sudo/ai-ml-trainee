#Create a class with constructor and destructor methods.
class Student:
    def __init__(self,name,department):
        self.name=name
        self.depart=department
        print("name is",self.name)
        print("department is",self.depart)
    def __del__(self):
        print("destructor is called")
        print("deleted")

s1=Student("Abhi","AIML trainee")
print(s1)
del s1
