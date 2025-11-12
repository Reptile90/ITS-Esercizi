from abc import ABC,abstractmethod

class Volo(ABC):
    
    def __init__(self, id_code:str, capacity:int):
        self.id_code:str = id_code
        self.capacity:int = capacity
        self.prenotazioni:int = 0
        
        
    @abstractmethod
    def prenota_posto(self):
        pass
    
    @abstractmethod
    def posti_disponibili(self):
        pass
        
        
        
class VoloCommerciale(Volo):
    def __init__(self, id_code:str, capacity:int):
        super().__init__(id_code, capacity)
        
        self.economy = capacity - ((capacity * 3)/100)
        
        self.business = capacity - ((capacity*8)/100)
        
        self.firstclass = capacity- self.economy-self.business
        
        self.prenotazioni_economy = 0
        
        self.prenotazioni_business = 0
        
        self.prenotazioni_first_class = 0
        
        
    def posti_disponibili(self)->dict[str,int]:
        
        posti_rimasti = self.capacity - self.prenotazioni
        
        posti_rimasti_economy = self.economy -self.prenotazioni_economy
        
        posti_rimasti_business = self.business-self.prenotazioni_business
        
        posti_rimasti_first = self.firstclass-self.prenotazioni_first_class
        return {
            "Posti Disponibili": posti_rimasti, 
            "Classe Economica":posti_rimasti_economy,
            "Classe Business":posti_rimasti_business,
            "Prima Classe":posti_rimasti_first
        }
        
    def prenota_posto(self,posti:int,classe_servizio:str):
        classe_servizio = classe_servizio.lower()
        if self.prenotazioni + posti > self.capacity:
            return "Non ci sono abbastanza posti disponibili sul volo"
        match classe_servizio:
            case "economy":
                if self.prenotazioni_economy + posti > self.economy:
                    return "Non ci sono abbastanza posti disponibili nella class Economy"
                self.prenotazioni_economy += posti
            
            case "business":
                if self.prenotazioni_business + posti > self.business:
                    return "Non ci sono abbastanza posti disponibili nella classe Business"
                self.prenotazioni_business += posti
                
            case "first class":
                if self.prenotazioni_first_class + posti > self.firstclass:
                    return "Non ci sono abbastanza posti disponibili nella Prima Classe"
                self.prenotazioni_first_class+= posti
            case _:
                return "Classe non valida"
            
        self.prenotazioni += posti
        print(f" Hai prenotato {posti} posti in classe {classe_servizio.capitalize()} sul volo {self.id_code}.")
        print(f" Totale prenotati in classe {classe_servizio.capitalize()}: {int(self.prenotazioni_economy if classe_servizio == 'economy' else self.prenotazioni_business if classe_servizio == 'business' else self.prenotazioni_first_class)}")
        
        
class VoloCharter(Volo):
    def __init__(self, id_code, capacity, prezzo:float):
        super().__init__(id_code, capacity)
        
        self.prezzo = prezzo
        
        
    def prenota_posto(self):
        if self.capacity > 0:
            self.prenotazioni = self.capacity
            print(f"Prenotati {self.capacity} posti sul volo Charter {self.id_code} al prezzo di {self.prezzo}")
            self.capacity = 0
            
            
    def posti_disponibili(self)->str:
        return f"Sono disponibili {self.capacity} posti sul volo Charter {self.id_code}"
    
    
class CompagniaAerea:
    
    def __init__(self,nome:str,prezzo_biglietto:float):
        
        self.nome = nome
        self.prezzo_biglietto = prezzo_biglietto
        self.flotta = []
        
    def aggiungi_volo(self,volo_commerciale:VoloCommerciale)->None:
        if volo_commerciale in self.flotta:
            print(f"Attenzione: Volo Commerciale {volo_commerciale} già presente")
            return
            
        self.flotta.append(volo_commerciale)
        
        
    def rimuovi_volo(self,volo_commerciale:VoloCommerciale)->None:
        if volo_commerciale not in self.flotta:
            print(f"Impossibile rimuovere il volo. Volo {volo_commerciale} non presente")
        self.flotta.remove(volo_commerciale)
        
    def mostra_flotta(self):
        return [volo.id_code for volo in self.flotta]
    
    def guadagno(self):
        prezzo_economy = self.prezzo_biglietto
        prezzo_business = self.prezzo_biglietto * 2
        prezzo_firstClass = self.prezzo_biglietto * 3
        totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                totale += (
                    volo.prenotazioni_economy * prezzo_economy +
                    volo.prenotazioni_business * prezzo_business +
                    volo.prenotazioni_first_class * prezzo_firstClass
                )
            elif isinstance(volo, VoloCharter):
                totale += volo.prenotazioni * volo.prezzo
        return round(totale, 2)

    
    
if __name__ == "__main__":
    
    FNC4020:VoloCommerciale = VoloCommerciale("FNC4020", 250)
    FNC3021:VoloCommerciale = VoloCommerciale("FNC3021", 180)
    NY09234:VoloCommerciale = VoloCommerciale("NY09234",300)        
    
    ETP2022:VoloCharter = VoloCharter("ETP2022",150,18000.00)
    CRT3147:VoloCharter = VoloCharter("CRT3147", 30, 1200.00)
    
    elitalia:CompagniaAerea = CompagniaAerea("Elitalia", 90.00)
    
    rianair:CompagniaAerea = CompagniaAerea("Rianair", 40.00)
    
                  
            
        
    print(FNC4020.posti_disponibili())
    print(FNC3021.posti_disponibili()) 
    
    FNC4020.prenota_posto(3,"Economy")
    FNC4020.prenota_posto(30,"business")
    FNC3021.prenota_posto(20,"first class")
    FNC3021.prenota_posto(42,"first class")
    
    
    print(ETP2022.posti_disponibili())
    
    ETP2022.prenota_posto()
    
    print(ETP2022.posti_disponibili())
    
    elitalia.aggiungi_volo(FNC3021)
    elitalia.aggiungi_volo(FNC4020)
    
    print(elitalia.mostra_flotta())
    elitalia.rimuovi_volo(FNC3021)
    
    rianair.aggiungi_volo(FNC3021)
    
    rianair.mostra_flotta()
    
    print(elitalia.guadagno())

    elitalia.aggiungi_volo(ETP2022)
    
    rianair.aggiungi_volo(NY09234)
    
    
    elitalia.mostra_flotta()
    rianair.mostra_flotta()
          