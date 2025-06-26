from typing import Self
from datetime import date
import re


class IntGEZ(int):
    
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n = int(v)
        if n >= 0:
            return super().__new__(cls, n)
        raise ValueError(f"Il valore {n} è minore di 0!")
    

class RealGEZ(float):
   
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n = float(v)
        if n >= 0:
            return super().__new__(cls, n)
        raise ValueError(f"Il valore {n} è minore di 0!")
    
class CodiceFiscale:
    pattern = re.compile(r'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$')

    def __init__(self, cf: str):
        if not self.is_valid(cf):
            raise ValueError("Codice Fiscale non valido")
        self.cf = cf

    @classmethod
    def is_valid(cls, cf: str) -> bool:
        return bool(cls.pattern.fullmatch(cf))

    def __str__(self):
        return self.cf
    

class Persona:
    __nome:str
    __cognome:str
    __cf:CodiceFiscale
    __data_nascita:date
    __is_uomo:bool
    __is_donna:bool
    __maternita:IntGEZ

    def set_nome(self,nome:str)->None:
        if isinstance(nome,str):
            self.__nome = nome
        else:
            raise ValueError("Errore, nome non valido. Il nome deve essere una stringa")

    def set_cognome(self,cognome:str)->None:
        if isinstance(cognome,str):
            self.__cognome = cognome
        else:
            raise ValueError("Errore, cognome non valido. Il cognome deve essere una stringa")

    def set_codice_fiscale(self,cf:CodiceFiscale):
        if isinstance(cf,CodiceFiscale):
            self.__cf = cf
        else:
            raise ValueError("Errore, Codice Fiscale non valido")
    
    def set_data_nascita(self, data_nascita: date):
        if not isinstance(data_nascita, date):
            raise ValueError("Errore, data di nascita non valida")
        if data_nascita > date.today():
            raise ValueError("La data di nascita non può essere nel futuro")
        self.__data_nascita = data_nascita
    
    def set_is_uomo(self,is_uomo:bool):
        if isinstance(is_uomo,bool):
            self._is_uomo = is_uomo
        else:
            raise ValueError ("is_uomo deve essere un booleano")
        
    def set_is_donna(self,is_donna:bool):
        if isinstance(is_donna,bool):
            self._is_donna = is_donna
        else:
            raise ValueError ("is_donna deve essere un booleano")
        
    def set_maternita(self,maternita:IntGEZ):
        if isinstance(maternita,IntGEZ):
            self.__maternita = maternita
        else:
            raise ValueError ("Errore, maternita deve essere un IntGez")
    
    def set_posizione_militare(self,posizione_militare:str):
        if isinstance(posizione_militare,str) and self.get_is_uomo():
            self._posizione_militare = posizione_militare
        
    def __init__(self,nome:str,cognome:str,cf:CodiceFiscale,data_nascita:date,maternita:IntGEZ|None, posizione_militare:str, is_uomo:bool=False, is_donna:bool=False)->None:
        
        if is_uomo and is_donna:
            raise ValueError("Una persona non può essere sia uomo che donna")
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_codice_fiscale(cf)
        self.set_data_nascita(data_nascita)
        self.set_is_uomo(is_uomo)
        self.set_is_donna(is_donna)
        
        if is_donna and maternita != None:
            self.set_maternita(maternita)
        else:
            raise ValueError("Solo una donna può avere un valore di maternità diverso da 0")

        if is_uomo:
            self.set_posizione_militare(posizione_militare)
        else:
            if not isinstance(posizione_militare,str):
                raise ValueError("Una donna non può avere una posizione militare")


    def get_nome(self)->str:
        return self.__nome
    
    def get_cognome(self)->str:
        return self.__cognome
    
    def get_codice_fiscale(self)->CodiceFiscale:
        return self.__cf
    
    def get_data_nascita(self)->date:
        return self.__data_nascita
    
    def get_is_uomo(self)->bool:
        return self.__is_uomo
    
    def get_is_donna(self)->bool:
        return self.__is_donna
    
    def get_maternita(self)->IntGEZ:
        return self.__maternita
    
    def __str__(self):
        return f"Nome: {self.get_nome()}\
                \nCognome: {self.get_cognome()}\
                \nCodice Fiscale: {self.get_codice_fiscale()}\
                \nData di nascita {self.get_data_nascita()}\
                \nSesso: {"Uomo" if self.get_is_uomo() else "Donna" if self.get_is_donna() else "Non specificato"}\
                \nMaternità: {self.get_maternita()}"
    

class Studente(Persona):
    __matricola:IntGEZ
    __matricole: dict[IntGEZ, str] = dict()

    def set_matricola(self,matricola)->None:
        cf_str = str(self.get_codice_fiscale())
        if not isinstance(matricola,IntGEZ):
            raise ValueError("La matricola deve essere un Intero >= 0")
        if matricola in Studente.__matricole and Studente.__matricole[matricola] != cf_str:
            raise ValueError("Errore: la matricola è già assegnata a un altro studente")
        self.__matricola = matricola
        Studente.__matricole[matricola] = cf_str
    
    def __init__(self, nome:str, cognome:str, cf:CodiceFiscale, data_nascita:date, maternita:IntGEZ, matricola:IntGEZ, is_uomo:bool = False, is_donna:bool = False):
        super().__init__(nome, cognome, cf, data_nascita, maternita, is_uomo, is_donna)

        self.set_matricola(matricola)


    def get_matricola(self) -> IntGEZ:
        return self.__matricola
    

    def __str__(self):
        return super().__str__() + f"\nMatricola: {self.get_matricola()}"
    
    def remove_matricola(self):
        try:
            if hasattr(self, "_Studente__matricola"):
                Studente.__matricole.pop(self.__matricola, None)
        except:
            pass

    @classmethod
    def matricola_assegnata(cls, matricola: IntGEZ) -> bool:
        return matricola in cls.__matricole
    



    

