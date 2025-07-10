from abc import ABC, abstractmethod
from string import ascii_lowercase
from string import ascii_uppercase

class CodificatoreMessaggio(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def codifica(testoInChiaro):
        pass


class DecodificatoreMessaggio(ABC):
    def __init__(self,):
        super().__init__()

    def decodifica(testoCodificato):
        pass



class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self, chiave:int):
        self.chiave:int = chiave

    def codifica(self,testoInChiaro)->str:
        testoCodificato:str = ""
        for index, letter in enumerate(testoInChiaro):
            if letter.isalpha():
                if letter.islower():
                    alphabet = ascii_lowercase
                else:
                    alphabet = ascii_uppercase
                index = alphabet.index(letter)
                newposition= (index + self.chiave) % len(alphabet)
                testoCodificato += alphabet[newposition]
            else:
                testoCodificato += letter
        return testoCodificato


    def decodifica(self,testoCodificato)->str:
        
        testoDecriptato:str = ""
        for index, letter in enumerate(testoCodificato):
            if letter.isalpha():
                if letter.islower():
                    alphabet = ascii_lowercase
                else:
                    alphabet = ascii_uppercase
                index = alphabet.index(letter)
                newposition= (index + self.chiave) % len(alphabet)
                testoDecriptato += alphabet[newposition]
            else:
                testoDecriptato += letter
        return testoDecriptato
    

    def scriviTesto(self,path:str, text:str)->None: 
        with open(path,"w",encoding="utf-8") as file:
            file.write(text)

    def leggiTesto(self,path:str)->str:
        with open(path, "r")as reader:
            text=reader.read()

        return text


class CifratoreACombinazione(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self, n:int):
        super().__init__()
        self.n = n

    def codifica(self, testoInChiaro)->str:
        temp_result= testoInChiaro
        for _ in range(self.n):
            temp_result = self.__combinatore(temp_result)
        return temp_result
        
            
            
        

           

            
    def __combinatore(self, testoInChiaro)->str:
        result = ""
        meta:int = len(testoInChiaro) // 2
        prima: str = testoInChiaro[:meta]
        seconda:str = testoInChiaro[meta:]
        if len(testoInChiaro)% 2 != 0:
            prima += seconda[0]
            seconda = seconda[1:]
        
        for i in range(len(seconda)):
            result += prima[i] + seconda[i]
        if len(prima)>len(seconda):
            result += prima[len(prima)-1]

        return result

    def decodifica(self,testoCodificato):
        new_text = testoCodificato
        
        
        for i in range(self.n):
            pari=""
            dispari=""
            for char in range(len(new_text)):
                if char % 2 ==0:
                    pari += new_text[char]
                else:
                    dispari += new_text[char]
            new_text = pari + dispari
        return new_text
    

    def scriviTesto(self,path:str, text:str)->None: 
        with open(path,"w",encoding="utf-8") as file:
            file.write(text)

    def leggiTesto(self,path:str)->str:
        with open(path, "r")as reader:
            text=reader.read()

        return text

         

 '''### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.'''       

        
if __name__ == "__main__":
    report= ""
    cs1:CifratoreAScorrimento= CifratoreAScorrimento(3)

    text= cs1.leggiTesto("./RECUPERO_PYTHON/prova.txt")

    cs1.codifica(text)

    cs1.scriviTesto("./RECUPERO_PYTHON/prova.txt")


        
    