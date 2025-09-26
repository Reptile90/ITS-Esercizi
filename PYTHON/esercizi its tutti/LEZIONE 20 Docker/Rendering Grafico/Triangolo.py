from Forma import Forma

class Triangolo(Forma):
    def __init__(self, lato:int):
        self.forma = "Triangolo"
        self.lato = lato
        
        
    def getArea(self):
        area = (self.lato**2)/2
        return area
    
    
    def render(self):
        for riga in range(1, self.lato + 1):
            for colonna in range(1, riga + 1):
                if riga == 1 or riga == self.lato or colonna == 1 or colonna == riga:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
                
        