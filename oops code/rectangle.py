#Create a class Rectangle to calculate area and perimeter.

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    def parameter(self):
        return 2*(self.length+self.breadth)
    
rect=Rectangle(4,5)
print("area",rect.area())
print("parameter=",rect.parameter())
        
    