class Rectangle :
    def __init__(self,a,b):
        self.__length = a
        self.__width = b
        
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
        
    def area(self):
        print("Area of the rectangle : ",self.get_length()*self.get_width())
        
    def perimeter(self):
        print("Perimeter of the Rectengle : ",2*(self.get_width()+self.get_length()))
        
    def display(self):
        self.area()
        self.perimeter()
    
R1 = Rectangle(10,5)
# R1.area()
# R1.perimeter()
R1.display()