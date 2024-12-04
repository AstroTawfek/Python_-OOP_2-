class salaryNot_InrangeException(Exception):
    """Your salary is not valid"""
    def __init__(self, m):
        self.message = m
        super().__init__(m)

class Employee:
    def __init__(self, name, salary):
        print("Your salary info system is opened")
        self.name = name
        self.salary = salary

    def Displaysalary(self):
        try:
            if not (10000 <= self.salary <= 50000):
                raise salaryNot_InrangeException("Wrong salary: It must be between 10000 and 50000")
        except salaryNot_InrangeException as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred in the try block:", e)
        else:
            print("Your salary:", self.salary)

em = Employee("Tawfek", 6000)
em.Displaysalary()