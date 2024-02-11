# Write a program that calculates the total salary of an employee based on the following criteria:
# If the employee has served for more than 10 years, he/she gets a bonus of 12% of the salary.
# If the employee has served for 6 to 10 years, he/she gets a bonus of 10% of the salary.
# If the employee has served for less than 6 years, he/she gets a bonus of 8% of the salary.
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