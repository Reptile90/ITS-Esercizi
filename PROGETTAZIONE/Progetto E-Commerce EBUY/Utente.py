from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from Index import Index

index_username = Index[str, "Utente"]("UtentiRegistrati")

class Utente(ABC):
    __username: str  # <<immutable>>
    __registrazione: datetime  # <<immutable>>

    def __init__(self, username: str):
        if index_username.get(username) is not None:
            raise ValueError(f"Username '{username}' già esistente!")
        self.__username = username
        self.__registrazione = datetime.now()
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









        

    


