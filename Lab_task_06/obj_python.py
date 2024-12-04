class Student :
    def __init__(self,a,id):
        self.name = a
        self.id = id
    def display(self):
        print("Name : ",self.name)
        print("Id : ", self.id)

s1 = Student("Tawfek", 1827)
s1.display()
print(s1.name)

s2 = Student("NeS" , 1813)
print(s2.name , s2.id)
s2.display()