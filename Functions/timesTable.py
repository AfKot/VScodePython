#Times Table Challenge

def timesTable(n):
    line = ""
    for row in range(1, n+1):
        for column in range(1, n+1):
            line = line + str(row*column) + "\t"
        line = line + "\n"
    print(line) #TO CHANGE THIS TO A FUNCTION CHANGE THIS TO RETURN LINE INSTEAD OF PRINT

number = int(input("Enter number: ")) 
timesTable(number)