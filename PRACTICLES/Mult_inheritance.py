class Person:
    def person_info(self, name, age):
        print("inside Person class")
        print(f"Name: {name}, Age: {age}")
class Company:
    def company_info(self, company_name, location):
        print("Inside Company class")
        print(f"Name: {company_name} , location: {location}")
class Employee(Person, Company):
    def Employee_info(self, salary, skills):
        print("Inside Employee class")
        print(f'Salary: {salary}, Skills: {skills}')
emp = Employee()
emp.person_info("David", 22)
emp.company_info("Google", "Atlanta")
emp.Employee_info(120000, "DevOps Engineer")