from datetime import date
from enum import StrEnum
import re

class Nazione:
    def __init__(self, nome:str):
        self.setNome(nome)

    def setNome(self, nome)->None:
        if not isinstance(nome,str):
            raise ValueError("Il nome della nazione deve essere una stringa")
        self.nome:str = nome

class Regione:
    def __init__(self, nome:str):
        self.setNome(nome)

    def setNome(self, nome)->None:
        if not isinstance(nome,str):
            raise ValueError("Il nome della regione deve essere una stringa")
        self.nome:str = nome

class Citta:
    def __init__(self,nome:str):
        self.setNome(nome)

    def setNome(self, nome)->None:
        if not isinstance(nome,str):
            raise ValueError("Il nome della città deve essere una stringa")
        self.nome:str = nome

class CodiceFiscale:
    pattern = re.compile(r'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$')

    def __init__(self, cf: str):
        if not self.is_valid(cf):
            raise ValueError("Codice Fiscale non valido")
        
    @classmethod
    def is_valid(cls, cf: str) -> bool:
        return bool(cls.pattern.fullmatch(cf))

    
class Indirizzo:
    _via:str
    _civico:int
    _cap:int

    def __init__(self, via:str, civico:int,cap:str) -> None:
        self._via = via
        self._civico = civico
        
        if not cap.isdigit() or len(cap) != 5:
            raise ValueError("Errore, inserisci un CAP numerico di 5 cifre")
        self._cap = cap

    def via(self) -> str:
        return self._via
    
    def civico(self) -> int:
        return self._civico
    
    def cap(self) -> str:
        return self._cap

    def __str__(self) -> str:
        return f"{self.via()}, {self.civico()}, CAP: {self.cap()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Indirizzo) or hash(self) != hash(other):
            return False
        else:
            return (self.via(), self.civico(),self.cap() ) == (other.via(), other.civico(), other.cap())

    def __hash__(self)->int: 
        return hash((self.via(), self.civico(),self.cap()))
    
class PartitaIva:
    pattern = re.compile(r'^\d{11}$')
    def __init__(self, partitaIva: str):
        if not self.is_valid(partitaIva):
            raise ValueError("Partita Iva non valida")
        self.partitaIva = partitaIva

    @classmethod
    def is_valid(cls, partitaIva: str) -> bool:
        return bool(cls.pattern.fullmatch(partitaIva))

    
class Telefono:
    pattern = re.compile(r'^\+?\d{6,15}$')
    def __init__(self, telefono: str):
        if not self.is_valid(telefono):
            raise ValueError(" Numero di telefono non valido")
        self.telefono = telefono

    @classmethod
    def is_valid(cls, telefono: str) -> bool:
        return bool(cls.pattern.fullmatch(telefono))
    def __str__(self):
        return self.telefono

    def __repr__(self):
        return f"Telefono('{self.telefono}')"



class Email:
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')
    def __init__(self, email: str):
        if not self.is_valid(email):
            raise ValueError(" Email non valida")
        self.email = email

    @classmethod
    def is_valid(cls, email: str) -> bool:
        return bool(cls.pattern.fullmatch(email))
    def __str__(self):
        return self.email

    def __repr__(self):
        return f"Email('{self.email}')"

class StatoOrdine(StrEnum):
    IN_PREPARAZIONE = "In Preparazione"
    INVIATO = "Inviato"
    DA_SALDARE = "Da saldare"
    SALDATO = "Saldato"

class Direttore:
    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, data_nascita: date, anni_servizio: int):
        self.setNome(nome)
        self.setCognome(cognome)
        self.setDataNascita(data_nascita)
        self.setAnniServizio(anni_servizio)
        self.setCodiceFiscale(cf)


    def setNome(self, nome)->None:
        if not isinstance(nome,str):
            raise ValueError("Il nome deve essere una stringa")
        self.nome:str = nome

    def setCognome(self,cognome)->None:
        if not isinstance(cognome,str):
            raise ValueError("IL cognome deve essere una stringa")
        self.cognome = cognome

    def setDataNascita(self, data_nascita: date)->None:
        if not isinstance(data_nascita, date):
            raise ValueError("La data di nascita deve essere un oggetto date")
        if data_nascita >= date.today():
            raise ValueError("La data di nascita non può essere nel futuro.")
        self.data_nascita = data_nascita

    def setAnniServizio(self, anni_servizio: int)->None:
        if not isinstance(anni_servizio, int) or anni_servizio < 0:
            raise ValueError("Gli anni di servizio devono essere un intero positivo")
        self.anni_servizio = anni_servizio

    def setCodiceFiscale(self,cf)->None:
        self.cf:CodiceFiscale = CodiceFiscale(cf)

    


class Dipartimento:
    def __init__(self, nome:str, indirizzo: Indirizzo):
        self.setNome(nome)
        self.setIndirizzo(indirizzo)
    
    def setIndirizzo(self,indirizzo)->None:
        if not isinstance(indirizzo,Indirizzo):
            raise ValueError("L'indirizzo deve essere un valore di Indirizzo")
        self.indirizzo = indirizzo


    def setNome(self,nome)->None:
        if not isinstance(nome, str):
            raise ValueError("Il nome del dipartimento deve essere una stringa")
        self.nome = nome


class Ordine:
    def __init__(self, dataStipula:date, imponibile:float, aliquotaIva:float, descrizione:str, stato:StatoOrdine):
        self.setImponibile(imponibile)
        self.setAliquotaIva(aliquotaIva)
        self.setDescrizione(descrizione)
        self.setDataStipula(dataStipula)
        self.setStato(stato)



    def setImponibile (self,imponibile)->None:
        if not isinstance(imponibile,float) or imponibile <= 0:
            raise ValueError("L'imponibile deve essere un numero decimale")
        self.imponibile = imponibile
    
    def setAliquotaIva(self,aliquotaIva)->None:
        if not isinstance(aliquotaIva,float) or aliquotaIva <= 0:
            raise ValueError("L'aliquota Iva deve essere un numero decimale e maggiore di 0")
        self.aliquotaIva = aliquotaIva

    def setDescrizione(self,descrizione)->None:
        if not isinstance(descrizione,str):
            raise ValueError ("La descrizione deve essere una stringa")
        self.descrizione = descrizione

    def setDataStipula(self,dataStipula)->None:
        if dataStipula > date.today():
            raise ValueError("La data deve minore o uguale alla data corrente")
        self.dataStipula = dataStipula
        
    
    def setStato(self, stato)->None:
        if not isinstance(stato, StatoOrdine):
            raise ValueError("Lo stato deve essere un valore di StatoOrdine")
        self.stato = stato



class Fornitore:
    def __init__(self, ragioneSociale: str, partitaIva:PartitaIva, indirizzo:Indirizzo, telefono:Telefono, email:Email):
        self.setRagioneSociale(ragioneSociale)
        self.setPartitaIva(partitaIva)
        self.setIndirizzo(indirizzo)
        self.setTelefono(telefono)
        self.setEmail(email)

    def setRagioneSociale(self, ragioneSociale)->None:
        if not isinstance(ragioneSociale,str):
            raise ValueError("La ragione sociale deve essere una stringa")
        self.ragioneSociale = ragioneSociale

    def setPartitaIva(self,partitaIva)->None:
        if not isinstance(partitaIva,PartitaIva):
            raise ValueError("La partita Iva deve essere un valore di PartitaIva")
        self.partitaIva = partitaIva

    def setIndirizzo(self,indirizzo)->None:
        if not isinstance(indirizzo,Indirizzo):
            raise ValueError("L'indirizzo deve essere un valore di Indirizzo")  
        self.indirizzo = indirizzo

    def setTelefono(self,telefono)->None:
        if not isinstance(telefono, Telefono):
            raise ValueError("Il numero di telefono deve essere un valore di Telefono")
        self.telefono = telefono

    def setEmail(self,email)->None:
        if not isinstance(email,Email):
            raise ValueError("L'email deve essere un valore di Email")
        self.email = email

    
    def __str__(self):
        return f"Ragione Sociale: {self.ragioneSociale}\nPartita Iva: {self.partitaIva.partitaIva}\nIndirizzo: {self.indirizzo}\nEmail: {self.email}\nTelefono: {self.telefono}"


if __name__ == "__main__":

    d1:Direttore = Direttore("Mario","Rossi", "RSSMRO43C22H501VE",23, 7)
    print(d1)
