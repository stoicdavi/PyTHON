#ensure proper user handling inputand provide meaningful error messages out put
import datetime
year_of_birth = int(input("Enter your year of birth:"))
height = float(input("Enter your height in metres:"))
#code to find the current year
current_year = datetime.datetime.now().year
#code to find the age

age = current_year - year_of_birth
print("Your age is:", age)
print("Your height is:", height)
print("Determining the type of the variables")
print("Your age is type:", type(age))
print("Your height is type:", type(height))