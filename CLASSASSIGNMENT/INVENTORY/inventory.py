from datetime import datetime
class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock
class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price
    #a function to display the products details
    def display(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nQuantity in Stock: {self.quantity_in_stock}\nUnit Price: {self.unit_price}"
class PerishableProduct(SimpleProduct):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date
    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price
    def display(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nQuantity in Stock: {self.quantity_in_stock}\nUnit Price: {self.unit_price}\nExpiry Date: {self.expiry_date}"
class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price
    def calculate_value(self):
        return self.quantity_in_stock * self.price
    def display(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nQuantity in Stock: {self.quantity_in_stock}\nPrice: {self.price}"

while True:
    print("1. Simple Product")
    print("2. Perishable Product")
    print("3. Digital Product")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        product_id = input("Enter product_id: ")
        name = input("Enter product name: ")
        quantity_in_stock = int(input("Quantity in Stock: "))
        unit_price = float(input("Enter the unit price: "))
        simple_product = SimpleProduct(name, product_id, quantity_in_stock, unit_price)
        print("\nProduct Details")
        simple_product.calculate_value()
        print(simple_product.display())
        file = open("inventory.txt", "a")
        file.write(simple_product.display())
        file.close()
    elif choice == 2:
        product_id = input("Enter product_id: ")
        name = input("Enter product name: ")
        quantity_in_stock = int(input("Quantity in Stock: "))
        unit_price = float(input("Enter the unit price: "))
        expiryDate = input("Enter the return date (YYYY-MM-DD): ")
        expiry_date = datetime.strptime(expiryDate, "%Y-%m-%d")
        perishable_product = PerishableProduct(name, product_id, quantity_in_stock, unit_price, expiry_date)
        print("\nProduct Details")
        perishable_product.calculate_value()
        print(perishable_product.display())
        file = open("inventory.txt", "a")
        file.write(perishable_product.display())
        file.close()
    elif choice == 3:
        product_id = input("Enter product_id: ")
        name = input("Enter product name: ")
        quantity_in_stock = int(input("Quantity in Stock: "))
        price = float(input("Enter the price: "))
        digital_product = DigitalProduct(name, product_id, quantity_in_stock, price)
        print("\nProduct Details")
        digital_product.calculate_value()
        print(digital_product.display())
        file = open("inventory.txt", "a")
        file.write(digital_product.display())
        file.close()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
