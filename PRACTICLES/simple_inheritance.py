class Animal:
    def legs(self):
        print("I have four legs with covered with fu")
class Dog(Animal):
    def ears(self):
        print("I have two very sensitive ears")
class Home(Dog):
    def myhome(self):
        print("My home is clean and ready for me")
d = Home()
d.ears()
