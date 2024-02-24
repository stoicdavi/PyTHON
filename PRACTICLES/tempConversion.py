class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def degree(self):
        faren = self.celsius * 1.8 +32
        return faren
temp = Temperature(4)
print(temp.degree())
