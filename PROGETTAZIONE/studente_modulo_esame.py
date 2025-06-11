from __future__ import annotations
from typing import Any


class Studente:
    _nome:str #noto alla nascita
    _esami:dict[Modulo, int]

    def set_nome(self,nome:str)->None:
        self.nome = nome
        self._esami = dict()
            
        

    def get_nome(self)->str:
        return self._nome


    def __init__(self, nome:str)->None:
        self.set_nome(nome)
        self._esami:dict = {}


    def esami(self)->frozenset[tuple[Modulo,int]]:
        return frozenset(self._esami.items())
    

    def add_esame(self,modulo:Modulo, voto:int):
        if modulo in self._esami:
            print(f"Lo studente{self.nome()} ha già superatol'esame {modulo._codice()}")
        else:
            self._esami[modulo]=voto


    def remove_esame(self, esame:Esame):
        if esame in self._esami:
            del self._esami[Modulo]
        else:
            print("Esame non presente")

    def media_voti(self)->float:
        if len(self._esami)== 0:
            raise RuntimeError (f"Lo studente {self.nome()} non ha superato alcun esame")
        return sum(self._esami.values()) / len(self._esami)

class Modulo:
    _codice:str

    def set_codice(self,codice:str)->None:
        if isinstance(codice,str):
            self._codice = codice

    def get_codice(self)->str:
        return self._codice
    
    def __init__(self, codice:str)->None:
        self.set_codice(codice)

class Esame:
    _studente:Studente
    _modulo:Modulo
    _voto:int

    def studente(self)->Studente:
        return self._studente
    
    def modulo(self)-> Modulo:
        return self._modulo
    
    def voto(self)->int:
        return self._voto
    
    def set_studente(self,studente:Studente)->Studente:
        self._studente = studente

    def set_modulo(self,modulo:Modulo)->Modulo:
        self._modulo = modulo
    
    def __init__(self, studente:Studente, modulo:Modulo, voto:int)->None:
        self.set_studente(studente)
        self.set_modulo(modulo)
        self._voto = voto

        
    def __hash__(self):
            return hash(self._studente,self._modulo)
    
    def __eq__(self, other:Any)->bool:
        if not isinstance(other,Esame):
            return False
        
        else:
            self._studente() == other._studente and self._modulo() == other._modulo



if __name__ == "__main__":

    stefano:Studente = Studente("Stefano")
    marcel:Studente = Studente 

    esami_stefano = stefano.esami()
    print(f"{stefano.nome} ha superato {len(esami_stefano)} esami")

    prog1:Modulo = Modulo("Progettazione 1")
    python14:Modulo = Modulo("Python.1-4")

    stefano.remove_esame(prog1)

    stefano.add_esame("Web", 31)

    media_stefano = stefano.media_voti()




    try:
        stefano.add_esame(modulo=python14, voto=31)

    except RuntimeError:
        print("L'esame è già presente")

    