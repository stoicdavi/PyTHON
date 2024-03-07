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
class PerishableProduct(SimpleProduct):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date
    def calculate_value(self):
        pass

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price
    def calculate_value(self):
        pass
product_id = input("Enter product_id: ")
name = input("Enter product name")
quantity_in_stock = int(input("Quantity in Stock"))
unit_price = float(input("Enter the unit price"))
expiryDate = input("Enter the return date (YYYY-MM-DD): ")
expiry_date = datetime.strptime(expiryDate, "%Y-%m-%d")
current_date = datetime.now()
shelflife = expiry_date - current_date

simple_product = SimpleProduct(name, product_id, quantity_in_stock, unit_price)
print(simple_product.calculate_value())

