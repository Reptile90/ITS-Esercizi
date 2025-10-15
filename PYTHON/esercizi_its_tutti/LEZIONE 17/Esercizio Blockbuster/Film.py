from __future__ import annotations
from typing import Self
class Film:
    def __init__(self, idCode:int, title:str):
        self.setID(idCode)
        self.setTitle(title)
        
        
    def setID(self,idCode:int)->None:
        if isinstance(idCode,int) and idCode > 0:
            self.__idCode:int = idCode
        else:
            print("L'identificativo deve essere un numero positivo")
            
    def setTitle(self,title:str)->None:
        if isinstance(title,str):
            self.__title:str = title
            
            
    def getID(self)->int:
        return self.__idCode
    
    def getTitle(self)->str:
        return self.__title
    
    
    def isEqual(self, otherFilm:Self):
        return True if self.getID() == otherFilm.getID() else False
    
    
    
        
        
    
            
            
    