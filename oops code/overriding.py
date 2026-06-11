#Demonstrate method overriding using inheritance.
class Person:
    def introduce(self):
        print("hii my self abhi")
class Student(Person):
    def introduce(self):
        print("i am student")

p=Person()
s=Student()
p.introduce()
s.introduce()