from abc import ABC, abstractmethod

class FormaGenerica(ABC): #abc è abstract base class

    @abstractmethod
    def draw(self)-> None:
        pass
    
    def setShape(self,shape:str)-> None:
        if shape:
            self.shape = shape
        else:
            print("La shape non può essere una stringa vuota")

    def getShape(self):
        return self.shape




