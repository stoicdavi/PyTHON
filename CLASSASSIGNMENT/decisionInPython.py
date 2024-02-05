salary = int(input("Enter your salary: "))
yearsOfService = int(input("Enter your years of service: "))
if yearsOfService > 10:
    bonus = salary * 0.12
elif yearsOfService >=6 and yearsOfService <= 10:
    bonus = salary * 0.10
elif yearsOfService < 6:
    bonus = salary * 0.08
totalSalary = salary + bonus
print("Your total salary is {} ".format(totalSalary))