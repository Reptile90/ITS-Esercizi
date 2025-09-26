from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, forma:str):
        super().__init__()
        self.forma = forma
        
    @abstractmethod
    def getArea():
        pass
    @abstractmethod
    def render():
        pass
    