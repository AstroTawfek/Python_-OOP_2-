"""
Scenario: 
A company has two types of employees: PermanentEmployee and ContractEmployee.
Both employee types have some shared details, such as name and id, but differ in how their
salaries are calculated. Permanent employees have a fixed monthly salary, while contract
employees are paid based on the number of hours worked.

Question:
Define a base class Employee with attributes name and id. Create two derived classes,
PermanentEmployee and ContractEmployee, that inherit from Employee. The
PermanentEmployee class should have a method calculate_salary() that returns a fixed monthly
salary, while ContractEmployee should have a method calculate_salary() that calculates salary
based on hourly rate and hours worked. Demonstrate this setup with appropriate test data.

"""


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        return f"Employee ID : {self.emp_id}\nName : {self.name}"


class PermanentEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_info(self):
        return f"{super().display_info()}\nMonthly Salary : ${self.monthly_salary:.2f}"


class ContractEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        return f"{super().display_info()}\nHourly Rate : ${self.hourly_rate:.2f}\nHours Worked : {self.hours_worked}\nTotal Salary : ${self.calculate_salary():.2f}"


# Creating instances of PermanentEmployee and ContractEmployee
perm_emp = PermanentEmployee("Tawfek", 1827, 19000)
contract_emp = ContractEmployee("Tuhin", 1815, 50, 160)

# Displaying employee information and calculated salaries
print(perm_emp.display_info())
print(f"Calculated Salary: ${perm_emp.calculate_salary():.2f}\n")

print(contract_emp.display_info())
print(f"Calculated Salary: ${contract_emp.calculate_salary():.2f}")