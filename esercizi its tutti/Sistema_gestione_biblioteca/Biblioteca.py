from Libro import Libro

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro:Libro)->str:
        self.catalogo.append(libro)
        return f"Libro '{libro.titolo}' aggiunto al catalogo"
    
    def presta_libro(self, titolo:str)->str:
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                return libro.in_prestito()
        return f"Il libro '{titolo}' non è presente nel catalogo."
                
    def restituisci_libro(self,titolo:str)->str:
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                return libro.restituzione()
        return f"Il libro '{titolo}' non è presente nel catalogo."
    
    def libri_disponibili(self)->list:
        libri_disponibili = []
        for libro in self.catalogo:
            if libro.stato_prestito == True:
                libri_disponibili.append(libro.titolo)
        if len(libri_disponibili)  > 0:
            stato_libri= "Libri disponibili:\n"
            for titolo in libri_disponibili:
                stato_libri += titolo + "\n"
            return stato_libri.strip()
        else:
            return "Nessun libro disponibile al momento."
    
    def mostra_stato_libri(self):
        risultato = ""
        for libro in self.catalogo:
            risultato += str(libro) + "\n"
        return risultato.strip()