from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, fly_code: str, capacity: int):
        self.fly_code = fly_code
        self.capacity = capacity
        self.reservations = 0

    @abstractmethod
    def prenota_posto(self, posti: int, classe_servizio: str):
        pass

    @abstractmethod
    def posti_disponibili(self) -> dict:
        pass


class VoloCommerciale(Volo):
    def __init__(self, fly_code: str, capacity: int):
        super().__init__(fly_code, capacity)
        self.posti_economica = int(self.capacity * 0.7)
        self.posti_business = int(self.capacity * 0.2)
        self.posti_prima = int(self.capacity * 0.1)
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self) -> dict[str, int]:
        return {
            "Classe Economica": self.posti_economica - self.prenotazioni_economica,
            "Classe Business": self.posti_business - self.prenotazioni_business,
            "Prima Classe": self.posti_prima - self.prenotazioni_prima
        }

    def prenota_posto(self, posti: int, classe_servizio: str)->None:
        disponibili = self.posti_disponibili()
        if self.capacity == 0:
            print(f"Volo {self.fly_code} al completo, non è possibile prenotare")
            return

        if classe_servizio not in disponibili:
            print("Classe non valida.")
            return

        if disponibili[classe_servizio] < posti:
            print(f"Posti insufficienti in {classe_servizio}.")
            return

        if classe_servizio == "Classe Economica":
            self.prenotazioni_economica += posti
            self.capacity -= posti
        elif classe_servizio == "Classe Business":
            self.prenotazioni_business += posti
            self.capacity -= posti
        elif classe_servizio == "Prima Classe":
            self.prenotazioni_prima += posti
            self.capacity-= posti
        print(f"Prenotazione volo {self.fly_code} di {posti} posti in {classe_servizio} effettuata.")

class VoloCharter(Volo):
    def __init__(self, fly_code:str, capacity:int, costo_charter:float):
        super().__init__(fly_code,capacity)
        self.costo_charter = costo_charter

    def prenota_posto(self)->None:
        
        if self.capacity == 0:
            print(f"Volo {self.fly_code} già al completo, non è possibile prenotare")
        else:
            self.capacity = 0
            print(f"Volo {self.fly_code} prenotato al costo di €{self.costo_charter}")

    def posti_disponibili(self):
        return f"{self.capacity} Posti disponibili sul volo {self.fly_code}"
            

class CompagniaArea:
    def __init__(self, nome:str, prezzo_standard:float):
        self.nome = nome
        self.prezzo_standard = prezzo_standard
        self.flotta = []
    
    def aggiungi_volo(self, volo_commerciale:VoloCommerciale)->None:
        if volo_commerciale not in self.flotta:
            self.flotta.append(volo_commerciale)
            print(f"Volo {volo_commerciale.fly_code} aggiunto correttamente")
        else:
            print(f"ERRORE! Volo {volo_commerciale.fly_code} già presente")

    def rimuovi_volo(self, volo_commerciale:VoloCommerciale)->None:
        if volo_commerciale in self.flotta:
            self.flotta.remove(volo_commerciale)
            print(f"Volo {volo_commerciale} rimosso correttamente")
        else:
            print(f"ERRORE! Volo non presente, impossibile rimuovere")


    def mostra_flotta(self):
        for volo in self.flotta:
            print(f"Codice volo: {volo.fly_code}")
    
    def guadagno(self)->float:
        guadagno:float = 0.0
        for volo in self.flotta:
            if isinstance(volo,VoloCommerciale):
                guadagno += ((volo.prenotazioni_economica * self.prezzo_standard )+ (volo.prenotazioni_business * self.prezzo_standard *2 )+ (volo.prenotazioni_prima * self.prezzo_standard * 3))
        return f"La compagnia {self.nome} ha guadagnato €{guadagno:.2f} con la prenotazione dei voli"

    
        


if __name__ == "__main__":

    report:list[str]= []
    volo1 = VoloCommerciale("COM123", 100)
    report.append(str(volo1.posti_disponibili()))
    volo1.prenota_posto(70, "Classe Economica")
    report.append(str(volo1.posti_disponibili()))
    volo1.prenota_posto(20, "Classe Business")
    report.append(str(volo1.posti_disponibili()))
    volo1.prenota_posto(11, "Prima Classe")
    report.append(str(volo1.posti_disponibili()))
    volo1.prenota_posto(10, "Prima Classe")
    report.append(str(volo1.posti_disponibili()))
    volo1.prenota_posto(2, "Prima Classe")

    voloCharter1 = VoloCharter("CHA456", 200, 20000)
    report.append(voloCharter1.posti_disponibili())
    voloCharter1.prenota_posto()
    voloCharter1.prenota_posto()

    volo2 = VoloCommerciale("COM456", 200)
    volo2.prenota_posto(100, "Classe Economica")

    CompagniaITA = CompagniaArea("ITA", 549.99)
    CompagniaITA.aggiungi_volo(volo1)
    CompagniaITA.aggiungi_volo(volo2)
    CompagniaITA.mostra_flotta()

    report.append(CompagniaITA.guadagno())

    
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in report:
            file.write(line + "\n")


        


