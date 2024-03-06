class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name


class SalayEmployee(Employee):
    def __init__(self, emp_id, name, salary, months, weekly_salary):
        super().__init__(emp_id, name)
        self.salary = salary
        self.months = months
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        salary = self.weekly_salary
        return salary


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        salary = self.hours_worked * self.hourly_rate
        return salary
    
    def display(self):
        print("Employee ID: ", self.emp_id)
        print("Employee Name: ", self.name)
        print("Hours Worked: ", self.hours_worked)
        print("Hourly Rate: ", self.hourly_rate)
        print("Payroll: ", self.calculate_payroll())


class CommisionedEmployee(SalayEmployee):
    def __init__(self, emp_id, name, salary, months, weekly_salary, commision_rate, sales):
        super().__init__(emp_id, name, salary, months, weekly_salary)
        self.commision_rate = commision_rate
        self.sales = sales

    def calculate_payroll(self):
        salary = self.weekly_salary + (self.commision_rate * self.sales)
        return salary


while True:
    print("\n****Welcome to the Payroll System****\n")
    print("Please Enter \n1 for Salary Employee\n2 for Hourly Employee\n3 for Commisioned Employee \n4 to exit")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        months = int(input("Enter months worked: "))
        weekly_salary = float(input("Enter weekly salary: "))
        emp = SalayEmployee(emp_id, name, salary, months, weekly_salary)
        emp.display()
        
    elif choice == 2:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        hours_worked = int(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))
        emp = HourlyEmployee(emp_id, name, hours_worked, hourly_rate)
        print("Payroll: ", emp.calculate_payroll())
    elif choice == 3:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        months = int(input("Enter months worked: "))
        weekly_salary = float(input("Enter weekly salary: "))
        commision_rate = float(input("Enter commision rate: "))
        sales = float(input("Enter sales: "))
        emp = CommisionedEmployee(
            emp_id, name, salary, months, weekly_salary, commision_rate, sales)
        print("Payroll: ", emp.calculate_payroll())
    elif choice == 4:
        break
