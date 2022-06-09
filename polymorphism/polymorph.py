class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking")

class Cat(Animal):
    def __init__(self, name, fur_colour):
        super().__init__(name)
        self.fur_colour = fur_colour
    
    def speak(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print("Woof")

doggo = Dog("Scooby", "German Shep")
catto = Cat("Whiskers", "Grey")

doggo.speak()
catto.speak()