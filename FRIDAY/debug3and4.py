#Exercise 3
import pdb

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0: 
                return False
        return True #this was inside the for loop

#pdb.set_trace()
print(is_prime(2)) #ERROR HERE - prints none
print(is_prime(41))
print(is_prime(12))
print(is_prime(7))
print(is_prime(11))


#Exercise 4
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n += 1


print(item_list[4])