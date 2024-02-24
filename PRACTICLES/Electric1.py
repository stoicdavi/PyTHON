def kplc(ID, name, units):
    if units <= 199:
        charge = 1.2*units
    elif units >= 200 and units < 400:
        charge = units*1.5
    elif units >= 400 and units < 600:
        charge = units * 1.8
    elif units >= 600:
        charge = units * 2
    return charge
ID = int(input("Enter your ID: "))
name = input("Enter your name : ")
units = int(input("enter units: "))
print(kplc(ID, name, units))
