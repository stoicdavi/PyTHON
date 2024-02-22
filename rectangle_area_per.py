class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area1 = self.length * self.width
        return area1
    def perimeter(self):
        per = 2 * self.length + 2 * self.width
        return per
length = int(input("Enter the Length: "))
width = int(input("Enter your length: "))
rectangle = Rectangle(length, width)
print(f'The are of the Rectangle is: {rectangle.area()}')
print(f'The perimeter is : {rectangle.perimeter()}')
