from Classe_Persona import Person

class Student(Person):
    def __init__(self, name:str, surname:str, age:int, cf:str, group:str=None):
        super().__init__(name, surname, age, cf)
        self.group = group

    def set_group(self, group: str) -> None:
        if group:
            self.group = group
        else:
            raise ValueError("Il gruppo di appartenenza non può essere una stringa vuota")
    def __str__(self) -> str:
        base = super().__str__()
        if self.group:
            group_info = f"Gruppo di studio: {self.group}"
        else:
            group_info = "Gruppo di studio: Nessun gruppo assegnato"
        return f"{base}\n{group_info}"