from __future__ import annotations
from typing import *
from weakref import WeakValueDictionary
from abc import ABC,abstractmethod
from datetime import datetime

KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')

"""
	An instance of this class defines an index over a set of objects
"""

class Index(Generic[KeyType, ValueType]):
	_name:str
	_objects:WeakValueDictionary[KeyType, ValueType]

	def __init__(self, name:str):
		self._name:str = name
		self._objects:WeakValueDictionary[KeyType, ValueType] = WeakValueDictionary()

	def __str__(self)->str:
		return (f"Index {self.name()}:\n - length: {len(self._objects)}\n - keys = {[k for k in self._objects.keys()]}")

	def name(self)->str:
		return self._name

	def add(self, _id:KeyType, obj:ValueType)->None:
		if _id in self._objects:
			raise KeyError(f"Duplicate key {_id} for class {type(obj)}")
		self._objects[_id] = obj

	def remove(self, _id:KeyType)->None:
		if _id is not None:
			del self._objects[_id]

	def get(self, _id:KeyType)->ValueType|None:
		return self._objects.get(_id, None)

	def all(self)->Generator[ValueType, None, None]:
		return self._objects.values()

	def __len__(self)->int:
		return len(self._objects)
		
		
class RealGZ(float):
    
    def __new__(cls, value: float | int | str | bool ):
        ret = float.__new__(cls, value) 

        if ret < 0:
            raise ValueError (f"The value {value} must be >= 0")
        return ret

index_username = Index[str, "Utente"]("UtentiRegistrati")

class Utente(ABC):
    __username: str  # <<immutable>>
    __registrazione: datetime  # <<immutable>>

    def __init__(self, username: str):
        if index_username.get(username) is not None:
            raise ValueError(f"Username '{username}' già esistente!")
        self.__username:str = username
        self.__registrazione:datetime = datetime.now()
        index_username.add(username, self)

    @abstractmethod
    def get_ruolo(self) -> str:
        pass

    def get_username(self) -> str:
        return self.__username

    def get_registrazione(self) -> datetime:
        return self.__registrazione

    def cancella_registrazione(self) -> None:
        index_username.remove(self.get_username())
        print("Utente cancellato correttamente")
        

    def __str__(self):
        return self.get_username()

    def __repr__(self) -> str:
        return f"Username: {self.get_username()}\nData registrazione: {self.get_registrazione().isoformat()}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Utente) and self.get_username() == other.get_username()

    def __hash__(self):
        return hash(self.get_username())
        
        
class UtentePrivato(Utente):
    def __init__(self, username: str):
        super().__init__(username)
        self._ruolo = "Privato"
        self._link_bid: set[Bid_Ut._link] =set()

    def get_ruolo(self) -> str:
        return self._ruolo

    def add_link_bid_ut(self, link: Bid_Ut._link) -> None:
        if link.utente() is not self:
            raise ValueError("Il link non riguarda questo utente.")
        self._link_bid.add(link)

    def __repr__(self):
        return f"Username: {self.get_username()}\nData registrazione: {self.get_registrazione()}\nTipologia Utente: {self._ruolo}"
        
        
class Bid:
    __istanteBid: datetime
    __utente: Utente

    def __init__(self, utente: Utente):
        self.__istanteBid = datetime.now()
        self.__utente = utente
        self._link_bid: set[Bid_Ut._link] = set()
        self._link_bid_asta: set[Asta_Bid._link] = set()

    def getIstanteBid(self) -> datetime:
        return self.__istanteBid

    def getUtente(self) -> Utente:
        return self.__utente

    def add_link_bid_ut(self, link: 'Bid_Ut._link') -> None:
        if link.bid() is not self:
            raise ValueError("Il link non riguarda questo bid.")
        self._link_bid.add(link)

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.bid() is not self:
            raise ValueError("Il link non riguarda questo bid.")
        self._link_bid_asta.add(link)


    def __repr__(self):
        return f"Username:{self.__utente.get_username()},Data Bid: {self.__istanteBid.isoformat()}"
        
class Asta:
    _prezzo_bid: RealGZ

    def __init__(self, prezzo: RealGZ, prezzo_bid: RealGZ, pubblicazione: datetime, scadenza: datetime):
        if pubblicazione >= scadenza:
            raise ValueError("La scadenza deve essere successiva alla data di pubblicazione.")
        self.prezzo:RealGZ = prezzo
        self._prezzo_bid:RealGZ = prezzo_bid
        self.pubblicazione:datetime = pubblicazione
        self.scadenza:datetime = scadenza
        self._insieme_bid: set['Bid'] = set()
        self._link_bid: set['Asta_Bid._link'] = set()
        
    
    def set_prezzo(self, prezzo:RealGZ):
        if self.is_scaduta() or self._link_bid:
            raise ValueError("Non è possibile cambiare il prezzo")
        self.prezzo = prezzo    
        
    def set_scadenza(self, scadenza:datetime)->None:
        if self.is_scaduta() or self._link_bid:
            raise ValueError ("Non è possibile inserire una nuova scadenza")
        if scadenza < datetime.now():
            raise AttributeError("Non è possibile inserire una scadenza minore della data di oggi")
        self.scadenza= scadenza
        

    def aggiungi_bid(self, bid: 'Bid') -> None:
        if bid.getIstanteBid() > self.scadenza:
            raise ValueError("Bid non valido. Il bid è stato effettuato dopo la scadenza dell'asta.")
        if bid in self._insieme_bid:
            raise ValueError("Questo bid è già stato registrato.")
        self._insieme_bid.add(bid)

    def prezzo_attuale(self, istante: datetime) -> RealGZ:
        quantita = 0
        for b in self._insieme_bid:
            if b.getIstanteBid() <= istante:
                quantita += 1
        return RealGZ(self.prezzo + quantita * self._prezzo_bid)


    def ultimo_bid(self, istante: datetime) -> Bid | None:
        ultimo_bid_valido = list(self._insieme_bid)[0]
        for b in self._insieme_bid:
            if b.getIstanteBid() <= istante:
                if (ultimo_bid_valido is None or b.getIstanteBid() > ultimo_bid_valido.getIstanteBid()):
                    ultimo_bid_valido = b
        return ultimo_bid_valido

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.asta() is not self:
            raise ValueError("Il link non riguarda questa asta.")
        self._link_bid.add(link)

    def is_scaduta(self) -> bool:
        return datetime.now() > self.scadenza

    def vincitore(self) -> Utente | None:
        if not self._insieme_bid:
            return None
        bid_finale = self.ultimo_bid(self.scadenza)
        return bid_finale.getUtente()
        
        
class Bid_Ut:
    @classmethod
    def add(cls, u: UtentePrivato, b: Bid) -> None:
        l = Bid_Ut._link(u, b)
        u.add_link_bid_ut(l)
        b.add_link_bid_ut(l)

    class _link:
        def __init__(self, utente: UtentePrivato, bid: Bid):
            self._utente = utente
            self._bid = bid

        def utente(self) -> UtentePrivato:
            return self._utente

        def bid(self) -> Bid:
            return self._bid

        def __repr__(self):
            return f"Bid_Ut (Utente={self._utente}, Bid={self._bid})"

        def __eq__(self, other: Any) -> bool:
            return (
                isinstance(other, Bid_Ut._link) and self._utente == other._utente and self._bid == other._bid)
        def __hash__(self):
            return hash((self.utente(), self.bid()))
    
    
class Asta_Bid:
    @classmethod
    def add(cls, a: Asta, b: Bid) -> None:
        l = Asta_Bid._link(a, b)
        a.add_link_asta_bid(l)
        b.add_link_asta_bid(l)
           
    class _link:
        def __init__(self, asta: Asta, bid: Bid):
            self._asta = asta
            self._bid = bid
            
        def asta(self) -> Asta:
            return self._asta

        def bid(self) -> Bid:
            return self._bid

        def __repr__(self):
            return f"Asta_Bid (Asta={self._asta}, Bid={self._bid}, Istante={self._bid.getIstanteBid().isoformat()})"

        def __eq__(self, other: Any) -> bool:
            return (
                isinstance(other, Asta_Bid._link) and self._asta == other._asta and self._bid == other._bid)
        def __hash__(self):
            return hash((self._asta, self._bid))
            
            
            
