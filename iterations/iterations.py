#ITERATIONS CHALLENGE
person = []

while len(person) < 5:
    p1 = input("What is your name? ")
    person.append(p1)

print('Class Register: ', person)
i = 0
while i < 5:
    print(person[i], "is awesome")
    i += 1
