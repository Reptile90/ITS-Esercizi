'''1. Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.'''


class Student:
    def __init__(self,name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(f" Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Study Program: {self.studyProgram}")

        
student_1 = Student("Stefano", "Python", 34, "Male")
student_2 = Student("Valentina","Python", 32, "Female")
student_3 = Student("Marcel", "Python", 24, "Male")

student_1.printInfo()
student_2.printInfo()
student_3.printInfo()


