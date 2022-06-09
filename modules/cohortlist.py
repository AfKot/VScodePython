cohortlist = ["Alexandra", "Chris", "John", "Judy", "Simon", "John"]

counter = 0
for x in cohortlist:
    if x == "John":
        counter +=1

print(f'The number of times the name John appeared: {counter}')