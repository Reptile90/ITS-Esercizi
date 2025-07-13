from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Utente import Utente
    from bid_ut import Bid_Ut
    from asta_bid import Asta_Bid

class Bid:
    __istanteBid: datetime
    __utente: Utente

    def __init__(self, utente: Utente):
        self.__istanteBid = datetime.now()
        self.__utente = utente
        self._link_bid: list['Bid_Ut._link'] = []
        self._link_bid_asta: list['Asta_Bid._link'] = []

    def getIstanteBid(self) -> datetime:
        return self.__istanteBid

    def getUtente(self) -> Utente:
        return self.__utente

    def add_link_bid_ut(self, link: 'Bid_Ut._link') -> None:
        if link.bid() is not self:
            raise ValueError("Il link non riguarda questo bid.")
        self._link_bid.append(link)

    def remove_link_bid_ut(self, link: 'Bid_Ut._link') -> None:
        if link in self._link_bid:
            self._link_bid.remove(link)

    def add_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link.bid() is not self:
            raise ValueError("Il link non riguarda questo bid.")
        self._link_bid_asta.append(link)

    def remove_link_asta_bid(self, link: 'Asta_Bid._link') -> None:
        if link in self._link_bid_asta:
            self._link_bid_asta.remove(link)

    def getLinkBidUt(self) -> list['Bid_Ut._link']:
        return list(self._link_bid)

    def getLinkAstaBid(self) -> list['Asta_Bid._link']:
        return list(self._link_bid_asta)

    def to_dict(self) -> dict:
        return {
            "username": self.__utente.get_username(),
            "data_bid": self.__istanteBid.isoformat(),
            "link_utente": [repr(link) for link in self._link_bid],
            "link_asta": [repr(link) for link in self._link_bid_asta]
        }

    def __repr__(self):
        return f"Username:{self.__utente.get_username()},Data Bid: {self.__istanteBid.isoformat()}"

    