class Animale:
    def __init__(self, nome, specie, eta, stato_adozione):
        
        self.nome = nome
        self.specie = specie
        self.eta = eta
        self.stato_adozione = stato_adozione
        
    def descrizione(self):
        return (f"Nome: {self.nome}"
                f"Specie: {self.specie}"
                f"Età: {self.eta}",
                f"Stato Adozione: {self.stato_adozione}"
                  )
        
        
class Rifiugio:
    def __init__(self):
        self.lista_animali =[]
        
    def add_animal(self, nome):
        if nome not in self.lista_animali:
            self.lista_animali.append(nome)
        raise ValueError("Animale già presente")
    
    def lista_animali(self):
        return "".join(self.lista_animali)
    
    