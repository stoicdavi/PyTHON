voterName = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
if age >= 18 and country == "Kenya":
    print("Dear {} You are from {} and {} years old and eligible to vote".format(voterName, country, age))
else:
    print("Sorry {} You are not 18 years eligible to vote".format(voterName))