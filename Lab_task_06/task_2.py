class Shape:
    def __init__(self,a):
        self.shape_name = a
    def get_name(self):
        print("The Shape is : ", self.shape_name)
        
        
class Rectangle(Shape) :
    def __init__(self,a,b):
        Shape.__init__(self , "Rectangle")
        self.length = a
        self.width = b
        
    def area(self):
        print("Area of the rectangle : ",self.length*self.width)
        
    def perimeter(self):
        print("Perimeter of the Rectengle : ",2*(self.length+self.width))
    
    def display(self):
        self.area()
        self.perimeter()
        self.get_name()
    
R1 = Rectangle(10,5)
# R1.area()
# R1.perimeter()
R1.display()