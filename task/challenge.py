#1/6
class Vehicle:
    def __init__(self, max_speed, mileage, colour="white"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

#2
vehicle1 = Vehicle(25, 250)
print(vehicle1.__dict__)

#3/5
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, colour="white", seat_cap=50):
        super().__init__(max_speed, mileage, colour)
        self.seat_cap = seat_cap

#4
bugg = Bus(100, 1200)
print(bugg.__dict__)

