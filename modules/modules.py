#Standard Modules
import math

number = float(input("Enter a number: "))
answer = math.sqrt(number)

print(answer)

import math
import random

def random_pi():
    return math.ceil(random.randint(1, 10) * math.pi)

for _ in range(5):
    print(random_pi())

#Importing Objects From Modules
from math import pi, floor
from random import randint

def random_pi():
    return ceil(randint(1, 10) * pi)

for _ in range(5):
    print(random_pi())