from Film import Film

class Azione(Film):
    def __init__(self, idCode, title, genre:str= 'Azione', penalty:float = 3.00):
        super().__init__(idCode, title)
        self.genre:str = genre
        self.penalty:float = penalty
        
    def getGenere(self)->str:
        return self.genre
    
    def getPenale(self)->float:
        return self.penalty
    
    def calcolaPenaleRitardo(self, giorniRitardo:int)->float:
        return self.getPenale() * giorniRitardo
    
    
    
class Commedia(Film):
    def __init__(self, idCode, title, genre:str = 'Commedia', penalty: float = 2.50):
        super().__init__(idCode, title)
        
        self.genre:str = genre
        self.penalty:float = penalty
        
    def getGenere(self)->str:
        return self.genre
    
    def getPenale(self)->float:
        return self.penalty
    
    def calcolaPenaleRitardo(self, giorniRitardo:int)->float:
        return self.getPenale() * giorniRitardo
    
    
class Drama(Film):
    def __init__(self, idCode, title, genre:str = 'Drama', penalty: float = 2.00):
        super().__init__(idCode, title)
        
        self.genre:str = genre
        self.penalty:float = penalty
        
    def getGenere(self)->str:
        return self.genre
    
    def getPenale(self)->float:
        return self.penalty
    
    def calcolaPenaleRitardo(self, giorniRitardo:int)->float:
        return self.getPenale() * giorniRitardo