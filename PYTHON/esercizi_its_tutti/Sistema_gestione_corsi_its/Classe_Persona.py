class Person:
    def __init__(self, name:str, surname:str, age:int, cf:str):
        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)
        self.set_cf(cf)

    #metodi setter
    def set_name(self, name)->None:
        if name:
            self.name = name
        else:
            raise ValueError ("Il nome non può essere una stringa vuota")
        
    def set_surname(self, surname)->None:
        if surname:
            self.surname = surname
        else:
            raise ValueError ("Il cognome non può essere una stringa vuota")
        
    def set_age(self, age)->None:
        if  age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
    def set_cf (self, cf)->None:
        if cf and len(cf) > 0:
            self.cf = cf
        else:
            raise ValueError("Il codice fiscale deve essere almeno di un carattere e non può essere una stringa vuota")
    
    #metodi getter
    def get_name(self)->str:
        return self.name
    
    def get_surname(self)-> str:
        return self.surname
    
    def get_age(self)->int:
        return self.age
    
    def get_cf(self)->str:
        return self.cf
    
    #metodo str per la stampa dei dati della persona
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.surname}\nEtà: {self.age}\nCodice Fiscale: {self.cf}"
