class Pagamento:
    def __init__(self)->None:
        
        self.__importo:float = 0.00
    
    def setImporto(self,importo:float)->None:
        if importo > 0 and isinstance(importo,float):
            self.__importo = importo
        else:
            print("L'importo deve essere un numero decimale maggiore di zero")
            
            
    def getImporto(self)->float:
        return self.__importo
    
    
    def dettagliPagamento(self)->str:
        return f"Importo del pagamento: €{self.getImporto():.2f}"
    
        