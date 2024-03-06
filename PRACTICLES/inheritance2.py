#inheritance
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def calculate_salary(self):
        pass
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, salary, hourly_rate, hours_worked):
        super().__init__(emp_id, name, salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary, months):
        super().__init__(emp_id, name, monthly_salary)
        self.monthly_salary = monthly_salary
        self.months = months
    def calculate_salary(self):
        return self.months * self.monthly_salary
        
#commisioned employee

class CommisonedEmployee(Employee):
    def __init__(self, emp_id, name, commision, totalSales):
        super().__init__(emp_id, name)
        self.commision = commision
        self.totalSales = totalSales
    def calculate_salary(self):
        return self.commision * self.totalSales
emp_id = int(input("Enter your Id"))   
name = input("Enter your name:")
Employ = CommisonedEmployee(emp_id, )

