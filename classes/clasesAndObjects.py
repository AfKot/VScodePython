#Exercises
#In a new Python file, create a class of students.

#It should contain the following attributes: name, age, and class with default value "student".

#It should also contain a method which takes in 3 test scores and prints the students average 
#test score.

#Creating class
class Students:

    def __init__(self, name, age, class_="Student"):
        self.name = name
        self.age = age
        self.class_ = class_
    def testscore(self, t1, t2, t3):
        total = ((t1+t2+t3)/30)*100
        return f'{self.name} your average score is: {total}%'

#Object of type Students
Dude1 = Students("Johnny", 35)

print(getattr(Dude1, "name"))
print(getattr(Dude1, "age"))
print(Dude1.testscore(10, 7, 8))