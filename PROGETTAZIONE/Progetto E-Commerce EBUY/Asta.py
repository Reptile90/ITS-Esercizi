from __future__ import annotations
from datetime import datetime
from RealGZ import RealGZ
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Bid import Bid
    from asta_bid import Asta_Bid
    from Utente import Utente

class Asta:
    _prezzo_bid: RealGZ

    def __init__(self, prezzo: RealGZ, prezzo_bid: RealGZ, pubblicazione: datetime, scadenza: datetime):
        if pubblicazione >= scadenza:
            raise ValueError("La scadenza deve essere successiva alla data di pubblicazione.")
        self.prezzo:RealGZ = prezzo
        self._prezzo_bid:RealGZ = prezzo_bid
        self.pubblicazione:datetime = pubblicazione
        self.scadenza:datetime = scadenza
        self.lista_bid: list['Bid'] = []
        self._link_bid: list['Asta_Bid._link'] = []
        
    
    def set_prezzo(self, prezzo:RealGZ):
        if self.is_scaduta() or self._link_bid:
            raise ValueError("Non è possibile cambiare il prezzo")
        self.prezzo = prezzo    
        
    def set_scadenza(self, scadenza:datetime)->None:
        if self.is_scaduta() or self._link_bid:
            raise ValueError ("Non è possibile inserire una nuova scadenza")
        if scadenza < datetime.now():
            raise AttributeError("Non è possibile inserire una scadenza minore della data di oggi")
        self.scadenza= scadenza
        

    def aggiungi_bid(self, bid: 'Bid') -> None:
        if bid.getIstanteBid() > self.scadenza:
            raise ValueError("Bid non valido. Il bid è stato effettuato dopo la scadenza dell'asta.")
        if bid in self.lista_bid:
            raise ValueError("Questo bid è già stato registrato.")
        self.lista_bid.append(bid)

    def prezzo_attuale(self, istante: datetime) -> RealGZ:
        quantita = 0
        for b in self.lista_bid:
            if b.getIstanteBid() <= istante:
                quantita += 1
        return RealGZ(self.prezzo + quantita * self._prezzo_bid)


    def ultimo_bid(self, istante: datetime) -> Bid | None:
        ultimo_bid_valido = None
        for b in self.lista_bid:
            if b.getIstanteBid() <= istante:
                if (ultimo_bid_valido is None or b.getIstanteBid() > ultimo_bid_valido.getIstanteBid()):
                    ultimo_bid_valido = b
        return ultimo_bid_valido

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.asta() is not self:
            raise ValueError("Il link non riguarda questa asta.")
        self._link_bid.append(link)

    def is_scaduta(self) -> bool:
        return datetime.now() > self.scadenza

    def vincitore(self) -> Utente | None:
        if not self.lista_bid:
            return None
        bid_finale = self.ultimo_bid(self.scadenza)
        return bid_finale.getUtente()
    

        