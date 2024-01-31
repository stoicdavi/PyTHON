#a code to check whether a voter is from easte african and allow him/she to vote if 18 yrs abnd above
age = int(input("Enter your age: "))
country = input("Enter your country: ")
if age >= 18 and country == "Kenya" or country == "Uganda" or country == "Tanzania" or country == "Rwanda" or country == "Burundi":
    print("You are eligible to vote")
else:
    print("Sorry You are not eligible to vote")