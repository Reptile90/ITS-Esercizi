from Pagamento import Pagamento

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self,nome_titolare:str,data_scadenza:str, numero_carta:str):
        super().__init__()
        
        self.setNomeTitolare(nome_titolare)
        self.setDataScadenza(data_scadenza)
        self.setNumeroCarta(numero_carta)
        
        
    def setNomeTitolare(self,nome_titolare:str)->None:
        if isinstance(nome_titolare,str):
            self.__nome_titolare = nome_titolare
        else:
            print("Nome titolare non valido. Il nome deve essere una stringa")
            
            
    def getNomeTitolare(self)->str:
        return self.__nome_titolare
    
    
    def setDataScadenza(self, data_scadenza:str)->None:
        if isinstance(data_scadenza,str):
            self.__data_scadenza = data_scadenza
        else:
            print("La data inserita non è valida")
        
        
    def getDataScadenza(self):
        return self.__data_scadenza
        
        
        
    def setNumeroCarta(self,numero_carta:str):
        if isinstance(numero_carta,str):
            self.__numero_carta = numero_carta
        else:
            print("Numero carta non valido")
            
    def getNumeroCarta(self)->str:
        return self.__numero_carta
            
            
            
    def dettagliPagamento(self):
        return (f"Pagamento con carta di credito: €{self.getImporto()}"
                f"Numero carta: {self.getNumeroCarta()}"
                f"Data di scadenza: {self.getDataScadenza()}"
                f"Titolare carta: {self.getNomeTitolare()}")
        
            
            
              
        
        