from __future__ import annotations
from typing import TYPE_CHECKING, Any
from datetime import datetime
import weakref

if TYPE_CHECKING:
    from Asta import Asta
    from Bid import Bid

class Asta_Bid:
    @classmethod
    def add(cls, a: Asta, b: Bid) -> None:
        l = Asta_Bid._link(a, b)
        a.add_link_asta_bid(l)
        b.add_link_asta_bid(l)

    @classmethod
    def remove(cls, l: weakref.ref[_link]) -> None:
        link = l()
        if link is not None:
            link.asta().remove_link_asta_bid(link)
            link.bid().remove_link_asta_bid(link)

    class _link:
        def __init__(self, asta: Asta, bid: Bid):
            self._asta = asta
            self._bid = bid
            self._istante = datetime.now()

        def asta(self) -> Asta:
            return self._asta

        def bid(self) -> Bid:
            return self._bid

        def getIstanteCreazione(self) -> datetime:
            return self._istante

        def to_dict(self) -> dict:
            return {
                "asta": repr(self._asta),
                "bid": repr(self._bid),
                "istante_creazione": self._istante.isoformat()
            }

        def __repr__(self):
            return f"Asta_Bid (Asta={self._asta}, Bid={self._bid}, Istante={self._istante.isoformat()})"

        def __eq__(self, other: Any) -> bool:
            return (
                isinstance(other, Asta_Bid._link)
                and self._asta == other._asta
                and self._bid == other._bid
            )
