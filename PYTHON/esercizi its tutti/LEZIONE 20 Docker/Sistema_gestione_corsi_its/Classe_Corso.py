from Classe_Gruppo import Group

class Course:
    def __init__(self, name:str):
        self.set_name(name)
        self.groups = []

    #metodo setter
    def set_name(self,name)->None:
        if name:
            self.name = name
        else:
            raise ValueError ("Il nome del corso non può essere una stringa vuota")
        
    #metodo getter
    def get_name(self)->str:
        return self.name
    def get_groups(self)->list:
        return self.groups
    
    #metodo per registrare gli studenti al corso
    def register(self,student)-> bool:
        for group in self.groups:
            if group.add_student(student):
                return True
        else:
            return False
        
    #metodo per aggiungere un gruppo di studenti
    def add_group(self, group)->None:
        if isinstance(group,Group):
            self.groups.append(group)
        else:
            raise ValueError("Errore: È possibile aggiungere solo oggetti di tipo Group al corso.")