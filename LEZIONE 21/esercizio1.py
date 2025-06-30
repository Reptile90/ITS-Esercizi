import re

class Documento:
    testo:str

    def __init__(self, text:str):
        self.setText(text)
    
    def setText(self,text):
        self.text = text


    def getText(self)->str:
        return self.text
    

    def isInText(self, word)->bool:

        pattern = re.compile(fr'^[{word}]$')
        
        return bool(pattern.search(self.text))
        
    

class Email(Documento):
    mittente:str
    destinatario:str
    messaggio:str

    def __init__(self, text:str , mittente:str, destinatario:str, titolo:str):
        super().__init__(text)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo)

    def setMittente(self,mittente):
        self.mittente = mittente

    def setDestinatario(self,destinatario):
        self.destinatario = destinatario

    def setTitolo(self,titolo):
        self.titolo = titolo

    def getMittente(self)->str:
        return self.mittente
    
    def getDestinatario(self)->str:
        return self.destinatario
    
    def getTitolo(self)->str:
        return self.titolo

    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitolo()}\nMessaggio: {self.getText()}"
    
    def writeToFile(self,path)->None:
        
        with open (path, "w") as file:
            file.write(self.getText)


class File(Documento):
    def __init__(self, nomePercorso):
        super().__init__()
        self.nomePercorso = nomePercorso

    def leggiTestoDaFile(self):
        try:
            with open(self.nomePercorso, 'r', encoding='utf-8') as file:
                self.testo = file.read()
        except FileNotFoundError:
            print(f"Errore: il file {self.nomePercorso} non esiste.")

    def getText(self):
        return f"{self.nomePercorso}\n{self.testo}"
    

if __name__ == "__main_":
    
    testo = "Ma chi ti credi di essere?"
    email1:Email= Email("Marcel","Lorenzo", "Una giornata particolare",testo)


    file1:File = File("/home/its/Esercizi/LEZIONE 21")

    email1.getText()
    



            

        
       


    