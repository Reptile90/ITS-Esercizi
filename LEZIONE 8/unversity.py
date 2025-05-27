from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, nome:str, age:int)->None:
        self.nome = nome
        self.age = age
    
    @abstractmethod
    def get_role(self)->str:
        pass

    def __str__(self)->str:
        return f"Name: {self.name}, Age: {self.age}, Role: {self.get_role()}"
    
class Student(Person):
    def __init__(self, nome:str, age:int, student_id:str)->None:
        super().__init__(nome, age)
        self.student_id = student_id
        self.courses:list[Course] = []

    def get_role(self)->str:
        return  "Student"
    
    def enroll(self, course)->None:
        if course not in self.courses:
         self.courses.append(course)

    def __str__(self)->str:
        return super().__str__() + f"ID: {self.student_id}"

class Professor(Person):
        def __init__(self, nome:str, age:int, professor_id:str, department:Department)->None:
            super().__init__(nome, age) 
            self.professor_id:str = professor_id
            self.department:Department = department
            self.courses:list[Course] = []
        def get_role(self):
            return "Professor"
        
        def assign_to_course(self,course)->None:
            if course not in self.courses:
                self.courses.append(course)

        def __str__(self):
            return super().__str__() + f"Professor ID: {self.professor_id} Department: {self.department}"
class Course:
    def __init__(self, course_name:str, code:str)->None: 
        self.course_name:str = course_name
        self.code:str = code
        self.students:list[Student] = []
        self.professor:Professor = None   

    def add_students(self, student:Student)->None:
        if student not in self.students:
            self.students.append(student)
    
    def set_professor(self,professor:Professor)->str:
        self.professor = professor

    def set_department(self, department_name)->None:
        self.department = department_name

    def __str__(self):
        if self.professor:  
            professor_name = self.professor
            return f"Course Name: {self.course_name}, Course ID: {self.code}, Professor: {professor_name}"
        else:
            return f"Course Name: {self.course_name}, Course ID: {self.code}, Professor: Non ancora assegnato"


class Department:
    def __init__(self, department_name:str)->None:
        self.department_name:str = department_name
        self.professors:list[Professor] = []
        self.courses:list[Course] = []

    def add_course(self, course:Course)->None:
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor)-> None:
        if professor not in self.professors:
            self.professors.append(professor)    

    def set_department(self)->None:
        self.department_name = Department    

    def __str__(self):
        if self.department_name

class University:
    def __init__(self, name:str)->None:
        self.university_name = name
        self.departments:list[Department] = []
        self.students:list[Student] = []

    def add_department(self, department:Department)->None:
        self.departments.append(department)

    def add_student(self,student:Student)->None:
        self.students.append(student)



if __name__== "__main__":
    univer:University = University("Sapieza")

    cs_dep:Department = Department("Informatica")
    lt_dep:Department = Department("Lettere")

    univer.add_department(cs_dep)
    univer.add_department(lt_dep)

    python_cs:Course = Course("Programmazione in Python","PY101")
    antica_cs:Course = Course("Lettere antiche", "LT101")

    cs_dep.add_course(python_cs)
    lt_dep.add_course(antica_cs)

    mc_prof:Professor = Professor("Marco Cascio", 18, "MC100")
    me_prof:Professor = Professor("Marco Esposito", 30,"ME100")


    cs_dep.add_professor(mc_prof)
    lt_dep.add_professor(me_prof)

    mc_prof.set_department(cs_dep)
    me_prof.set_department(lt_dep)

    python_cs.set_professor(mc_prof)
    antica_cs.set_professor(me_prof)


    student_leandro:Student = Student("Leandro Pazienza",27, "LPZ")
    student_cristiano:Student = Student("")