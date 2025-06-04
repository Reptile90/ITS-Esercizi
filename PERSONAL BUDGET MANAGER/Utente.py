class Utente:
    _nome:str
    _cognome:str

    def nome(self)-> str:
        return self._nome
    def cognome(self)-> str:
        return self._cognome
    
    def setNome(self, nome:str)->None:
        self._nome = nome
    
    def setCognome(self, cognome:str)->None:
        self._cognome = cognome


    def __init__(self, nome:str, cognome:str):
        self.setNome(nome)
        self.setCognome(cognome)

