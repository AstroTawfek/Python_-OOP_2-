class Rectangle :
    def __init__(self,a,b):
        self.length = a
        self.width = b
        
    def area(self):
        print("Area of the rectangle : ",self.length*self.width)
        
    def perimeter(self):
        print("Perimeter of the Rectengle : ",2*(self.length+self.width))
        
    def display(self):
        self.area()
        self.perimeter()
    
R1 = Rectangle(10,5)
# R1.area()
# R1.perimeter()
R1.display()