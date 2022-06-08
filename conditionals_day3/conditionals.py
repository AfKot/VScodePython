#MARK CHALLENGE
mark = int(input("How many marks did you receive? "))
if mark >= 90:
    print("Your grade: Distinction*")
elif mark >= 80:
    print("Your grade: Distinction")
elif mark >= 60:
    print("Your grade: Merit")
elif mark >= 40:
    print("Your grade: Pass")
else:
    print("FAIL")

