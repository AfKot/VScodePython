a = int(input("What number would you like the factorial of: "))

def fact(x):
    counter = 1
    for x in range(1, x+1):
        counter *= x
    return counter

print(fact(a))