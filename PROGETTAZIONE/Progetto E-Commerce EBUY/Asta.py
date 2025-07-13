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
        self.prezzo = prezzo
        self._prezzo_bid = prezzo_bid
        self.pubblicazione = pubblicazione
        self.scadenza = scadenza
        self.lista_bid: list['Bid'] = []
        self._link_bid: list['Asta_Bid._link'] = []

    def aggiungi_bid(self, bid: 'Bid') -> None:
        if bid.getIstanteBid() > self.scadenza:
            raise ValueError("Bid non valido. Il bid è stato effettuato dopo la scadenza dell'asta.")
        if bid in self.lista_bid:
            raise ValueError("Questo bid è già stato registrato.")
        self.lista_bid.append(bid)

    def prezzo_attuale(self, istante: datetime) -> RealGZ:
        quantita = len([b for b in self.lista_bid if b.getIstanteBid() <= istante])
        return RealGZ(self.prezzo + quantita * self._prezzo_bid)

    def ultimo_bid(self, istante: datetime) -> Bid | None:
        bid_valido = [b for b in self.lista_bid if b.getIstanteBid() <= istante]
        return max(bid_valido, key=lambda b: b.getIstanteBid()) if bid_valido else None

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.asta() is not self:
            raise ValueError("Il link non riguarda questa asta.")
        self._link_bid.append(link)

    def remove_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link in self._link_bid:
            self._link_bid.remove(link)

    def getLinkAstaBid(self) -> list['Asta_Bid._link']:
        return list(self._link_bid)

    def is_scaduta(self) -> bool:
        return datetime.now() > self.scadenza

    def vincitore(self) -> Utente | None:
        if not self.lista_bid:
            return None
        bid_finale = self.ultimo_bid(self.scadenza)
        return bid_finale.getUtente()

    def to_dict(self) -> dict:
        return {
            "prezzo": str(self.prezzo),
            "prezzo_bid": str(self._prezzo_bid),
            "pubblicazione": self.pubblicazione.isoformat(),
            "scadenza": self.scadenza.isoformat(),
            "scaduta": self.is_scaduta(),
            "vincitore": self.vincitore().get_username() if self.vincitore() else None,
            "numero_bid": len(self.lista_bid)
        }

        