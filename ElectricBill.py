from typing import Union
# Write a program to calculate the electricity bill. For the first 199 units, the charge is 1.20 per unit. For the next 200 units, the charge is 1.50 per unit. For the next 200 units, the charge is 1.80 per unit. For the next 200 units, the charge is 2.0 per unit. The program should accept the customer ID, customer name, and the number of units consumed and print the total charge using the customer name.
CustomerId = int(input("Enter your customer ID :"))
CustomerName = input("Enter your name :")
UnitConsumed: Union[int, float] = float(input("enter the units consumed: "))

def calculate(UnitConsumed: Union[int, float]) -> float:
    if UnitConsumed <= 199:
        charge = UnitConsumed * 1.20
    elif UnitConsumed >= 200 and UnitConsumed <= 400:
        charge = UnitConsumed * 1.50
    elif UnitConsumed >= 401 and UnitConsumed <= 600:
        charge = UnitConsumed * 1.80
    else:
        charge = UnitConsumed * 2.0
    return charge

print("Dear {} your total charge is {}".format(CustomerName, calculate(UnitConsumed)))
