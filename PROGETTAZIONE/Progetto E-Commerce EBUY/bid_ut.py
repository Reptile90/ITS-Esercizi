from __future__ import annotations
from typing import TYPE_CHECKING, Any
import weakref

if TYPE_CHECKING:
    from Bid import Bid
    from UtentePrivato import UtentePrivato

class Bid_Ut:
    @classmethod
    def add(cls, u: UtentePrivato, b: Bid) -> None:
        l = Bid_Ut._link(u, b)
        u.add_link_bid_ut(l)
        b.add_link_bid_ut(l)

    class _link:
        def __init__(self, utente: UtentePrivato, bid: Bid):
            self._utente = utente
            self._bid = bid

        def utente(self) -> UtentePrivato:
            return self._utente

        def bid(self) -> Bid:
            return self._bid

        def __repr__(self):
            return f"Bid_Ut (Utente={self._utente}, Bid={self._bid})"

        def __eq__(self, other: Any) -> bool:
            return (
                isinstance(other, Bid_Ut._link) and self._utente == other._utente and self._bid == other._bid
            )
