#Implement hierarchical inheritance using a common parent class
class Student:
    def name(self):
        print("Student name=abhi")
class Marks(Student):
    def get_marks(self):
        print("Total marks =29")
class Grade(Student):
    def get_grade(self):
        print("A grade student")
m = Marks()
g = Grade()

m.name()
m.get_marks()

print()
g.name()
g.get_grade()