#A simple python program to add two numbers
import sys
print("Welcome to our addition calculator")

#prompting the user to enter two numbers

num1 = int(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

answer=num1+num2
print(answer)
print(type(num1))
print(sys.getsizeof(num1))

##Checking whether num1 or num2 is greater
if num1 > num2:
    print("Number one is greateer")
else:
    print("Number two is greater")
