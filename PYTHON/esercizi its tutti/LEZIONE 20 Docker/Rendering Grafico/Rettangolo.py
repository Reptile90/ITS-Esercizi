from Forma import Forma

class Rettangolo(Forma):
    
    def __init__(self, base:int, altezza:int):
        self.forma = "Rettangolo"
        self.base = base
        self.altezza = altezza
        
    
    def getArea(self):
        area = (self.base * self.altezza)
        return area
        
        
    from Forma import Forma

class Rettangolo(Forma):
    
    def __init__(self, base: int, altezza: int):
        self.forma = "Rettangolo"
        self.base = base
        self.altezza = altezza
        
    def getArea(self):
        return self.base * self.altezza
        
    def render(self):
        for riga in range(self.altezza):
            for colonna in range(self.base):
                if riga == 0 or riga == self.altezza - 1 or colonna == 0 or colonna == self.base - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
                
        
        