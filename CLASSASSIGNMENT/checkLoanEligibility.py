#a code to check if a user is eligible for a loan
userName = input("Enter your name: ")
annualIncome = int(input("What is your annual income? "))
age = int(input("What is your age? "))
if annualIncome >= 21_000 and age >= 21:
    print("Congratulations, You qualify for a loan")
else:
    print("Unfortunately, we are unable to offer you a loan at this time")