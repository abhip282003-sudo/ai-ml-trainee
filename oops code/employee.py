#Create a class Employee with salary calculation functionality.
class Employee:
    def __init__(self,salary,day):
        self.salary=salary
        self.day=day
    def total_salary(self):
        return self.salary*self.day
    
emp=Employee(200,5)
print("totalsalary",emp.total_salary())
       