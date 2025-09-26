from Pagamento import Pagamento


class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()
        
    def dettagliPagamento(self):
        return f"Pagamento in contanti di: €{self.getImporto():.2f}"
    
    def inPezziDa(self)->str:
        tagli:list =[500,200,100,50,20,10,5,2,1,0.50,0.20]
        resto = self.getImporto()
        pezzi = {}
        
        for taglio in tagli:
            quantita = int(resto // taglio)
            if quantita > 0:
                pezzi[taglio]=quantita
                resto=round(resto - quantita * taglio, 2)
        
        print(f"{self.getImporto()} da pagare in contanti con:")
        for taglio, quantita in pezzi.items():
            tipo="Banconote" if taglio >= 5 else "monete"
            print(f"{quantita} {tipo} da {taglio}")
            
            
            
                
            
        
        
    
    