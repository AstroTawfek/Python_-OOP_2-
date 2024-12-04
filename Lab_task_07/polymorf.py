class Person:    
    def __init__(self, a, b):
        print("Person Constructor")        
        self.f_name = a        
        self.l_name = b
    
    def display(self):        
        print("Your First name : ", self.f_name)        
        print("Your last name : ", self.l_name)

class Student(Person):
    def __init__(self, a, b, g_year):
        print("Student constructor")
        super().__init__(a, b)
        self.g_year = g_year

    def display(self):
        print("Hello", self.f_name, self.l_name, ". Congrats for your graduation in the year", self.g_year)

class Teacher(Person):
    def __init__(self, a, b, j_year):
        print("Teacher constructor")
        super().__init__(a, b)
        self.j_year = j_year

    def display(self):
        print("Presenting respecter teacher", self.f_name, self.l_name, ". Congrats for your joining in the year", self.j_year)

class Admin(Person):
    def __init__(self, a, b, j_year):
        print("Admin constructor")
        super().__init__(a, b)
        self.j_year = j_year

    def display(self):
        print("Hello", self.f_name, self.l_name, ". Congrats for your joining in the year", self.j_year)
class Current_Student(Student):
    def __init__(self, a, b, g_year, id):
        print("current_Student constructor")
        super().__init__(a, b, g_year)
        self.id = id

    def display(self):
        print("Hello", self.f_name, self.l_name,"id ", self.id, ".You will be graduate in", self.g_year)
class Alumni_Student(Student):
    def __init__(self, a, b, g_year, id):
        print("Alumni_Student constructor")
        super().__init__(a, b , g_year)
        self.id = id

    def display(self):
        print("Hello", self.f_name, self.l_name, "id ", self.id ,". Congrats for your graduation in the year", self.g_year)

S1 = Current_Student("Muhammadullah", "Tawfek", 2026 , 1827)
S1.display()
S2 = Alumni_Student("Muhammadullah", "Tawfek", 2026 , 1234)
S1.display()
T1 = Teacher("Nasima islam", "Bithi", 2020)
T1.display()
A1 = Admin("wx", "yz", 2015)
A1.display()