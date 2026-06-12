#Implement encapsulation using private variables and getter/setter methods
class Student:
    def __init__(self,name,marks,percentage):
        self.name=name
        self.marks=marks
        self.__percentage=percentage
    def get_details(self):
        print("name is :",self.name)
        print("marks is",self.marks)
    
    def get_percentage(self):
        return self.__percentage
    def set_percentage(self, percentage):
        self.__percentage = percentage
get_d=Student("abhishek",454,56)
get_d.get_details()
print("percenatge is",get_d.get_percentage())
get_d.set_percentage(90)
print("new percentage",get_d.get_percentage())