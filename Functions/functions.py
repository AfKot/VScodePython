#Tutorial

def add_cal(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_cal(5,10)
print(added_number + 15)


#CHALLENGE

name = input("What's ya name? ")
h_score = int(input("What did you get in your homework? (out of 25) "))
a_score = int(input("What did you get in your assssment? (out of 50) "))
e_score = int(input("What did you get in your exam? (out of 100) "))

def grade(h_score, a_score, e_score):
    mark = ((h_score+a_score+e_score)/175)*100
    if mark >= 90:
        return f'{name}, you scored {mark}%, Grade: A'
    elif mark >= 75:
        return f'{name}, you scored {mark}%, Grade: B'
    elif mark >= 55:
        return f'{name}, you scored {mark}%, Grade: C'
    else:
        return f'{name}, you scored {mark}%, FAIL'

print(grade(h_score, a_score, e_score))