print("***welcome to the temperature converter***")

while True:
    print("welcome to the temperature converter")
    print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Exit")
  
    choice = int(input("Enter your choice: "))
    if choice == 1:
        c = float(input("Enter the temperature in Celsius: "))
        f = (c * 1.8) + 32
        print("The temperature in Fahrenheit is: ", round(f))
    elif choice == 2:
        f = float(input("Enter the temperature in Fahrenheit: "))
        c = (f - 32) / 1.8
        print("The temperature in Celsius is: ", round(c))
    elif choice == 3:
        
        break
    else:
        print("Invalid choice")
