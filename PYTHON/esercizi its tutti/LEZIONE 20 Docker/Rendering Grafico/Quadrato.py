from Forma import Forma

class Quadrato(Forma):
    
    def __init__(self, lato:int):
        
        self.forma = "Quadrato"
        
        self.lato = lato
        
        
    def getArea(self):
        area = self.lato ** 2
        return area


    def render(self):
        for riga in range(self.lato):
            for colonna in range(self.lato):
                if riga == 0 or riga == self.lato - 1 or colonna == 0 or colonna == self.lato - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()