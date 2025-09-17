class Libro:
    def __init__(self, titolo:str, autore:str):
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito = True
        
    #metodo per verificare se un libro è in prestito
    def in_prestito(self)->str:
        if self.stato_prestito:
            self.stato_prestito = False
            return f"Il libro {self.titolo} è in prestito"
        else:
            return f"Il libro {self.titolo} è già in prestito"
        
    #metodo per verificare se un libro è stato restituito
    def restituzione(self)->str:
        if not self.stato_prestito:
            self.stato_prestito = True
            return f"Il libro {self.titolo} è stato restituito"
        else:
            return f"Libro {self.titolo} disponibile"

    #stampa le informazioni del libro e lo stato
    def __str__(self):
        if self.stato_prestito == True:
            stato = "Disponibile"
            return f"Libro: {self.titolo}, Autore: {self.autore} Stato: {stato}"
        else:
            stato = "In Prestito"
            return f"Libro: {self.titolo}, Autore: {self.autore} Stato: {stato}"