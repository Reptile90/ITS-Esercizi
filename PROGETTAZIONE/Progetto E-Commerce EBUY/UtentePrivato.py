from __future__ import annotations
from Utente import Utente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bid_ut import Bid_Ut

class UtentePrivato(Utente):
    def __init__(self, username: str):
        super().__init__(username)
        self._ruolo = "Privato"
        self._link_bid: list[Bid_Ut._link] = []

    def get_ruolo(self) -> str:
        return self._ruolo

    def add_link_bid_ut(self, link: Bid_Ut._link) -> None:
        if link.utente() is not self:
            raise ValueError("Il link non riguarda questo utente.")
        self._link_bid.append(link)

    def __repr__(self):
        return f"Username: {self.get_username()}\nData registrazione: {self.get_registrazione()}\nTipologia Utente: {self._ruolo}"

    