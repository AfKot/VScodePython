#Superclass
class Animal:
    def __init__(self, name):
        self.name = name

#Sub class / Child class
class Cat(Animal): #when defining a child class we need to put the parent class in brackets
    def __init__(self, name, fur_colour):
        super().__init__(name) #calls methods from the parent class
        self.fur_colour = fur_colour

#objects
cat1 = Cat("Whiskers", "Brown")

print(cat1.__dict__)