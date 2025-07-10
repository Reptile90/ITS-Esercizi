from abc import ABC
from datetime import datetime
from Index import Index
from weakref import WeakValueDictionary
from typing import Self
class Utente(ABC):

    _username:str # <<immutable>>
    _registrazione:datetime # <<immutable>>
    _lista_username:WeakValueDictionary = Index(str,Self)("Username")

    def set__username(self,username:str):
        if username in _lista_username:
            pass



    def __init__(self, username:str, registrazione:datetime)->None:
        super().__init__()
        self.set__username(username)
        self._lista_username:WeakValueDictionary = Index(str,Self)("Username")



        

    


