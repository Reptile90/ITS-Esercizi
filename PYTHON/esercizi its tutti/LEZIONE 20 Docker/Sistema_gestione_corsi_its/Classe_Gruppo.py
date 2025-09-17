from Classe_Studente import Student
from Classe_Insegnante import Lecturer

class Group:
    def __init__(self, name:str, limit:int):
        self.set_name(name)
        self.set_limit(limit)
        self.students = []
        self.lecturers = []

    #metodi setter
    def set_name(self,name)->None:
        if name:
            self.name = name
        else:
            raise ValueError ("Il nome del gruppo non può essere una stringa vuota")
        
    def set_limit(self, limit) -> None:
        if isinstance(limit, int) and limit >= 0:
            self.limit = limit
        else:
            raise ValueError("Il limite deve essere un numero intero positivo")

    #metodi getter
    def get_name(self)->str:
        return self.name
    
    def get_limit(self)->int:
        return self.limit
    
    def get_students(self)->list:
        return self.students
    
    def get_limit_lecturers(self)->int:
        lecturers_limit= len(self.students) // 10
        
        if len(self.students) % 10 != 0 or len(self.students) == 0:
            lecturers_limit += 1
        return lecturers_limit
    
    #metodo per aggiungiere gli studenti
    def add_student(self, student) -> bool:
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self.name)
            return True
        else:
            return False
        
    #metodo per aggiungere gli insegnanti
    def add_lecturer(self, lecturer) -> bool:
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True
        else:
            print("Limite docenti raggiunto. Impossibile aggiungere il docente.")
            return False

    #metodo str per la stampa di studenti e insegnanti    
    def __str__(self) -> str:
        student_names = []
        for student in self.students:
            first_name = student.get_name()
            last_name = student.get_surname()
            full_name = f"{first_name} {last_name}"
            student_names.append(full_name)

        if len(student_names) > 0:
            student_list = ', '.join(student_names)
        else:
            student_list = "None"

        lecturer_names = []
        for lecturer in self.lecturers:
            first_name = lecturer.get_name()
            last_name = lecturer.get_surname()
            full_name = f"{first_name} {last_name}"
            lecturer_names.append(full_name)

        if len(lecturer_names) > 0:
            lecturer_list = ', '.join(lecturer_names)
        else:
            lecturer_list = "None"

        group_name = f"{self.name}"
        student_limit = f"{self.limit}"
        student_count = f"{len(self.students)}"
        lecturer_count = f"{len(self.lecturers)}"
        lecturer_limit = f"{self.get_limit_lecturers()}"

        result = (
            f"Group: {group_name}\n"
            f"Student limit: {student_limit}\n"
            f"Students ({student_count}): {student_list}\n"
            f"Lecturers ({lecturer_count}): {lecturer_list}\n"
            f"Current lecturer limit: {lecturer_limit}"
        )

        return result