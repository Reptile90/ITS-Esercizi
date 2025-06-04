class Bilancio:
    _totale: float
    _tetto_spesa: float

    def totale(self) -> float:
        return self._totale

    def tetto_spesa(self) -> float:
        return self._tetto_spesa

    def setTotale(self, totale: float):
        self._totale = totale

    def setTetto_spesa(self, tetto_spesa: float):
        self._tetto_spesa = tetto_spesa

    def __init__(self, totale: float, tetto_spesa: float):
        self.setTotale(totale)
        self.setTetto_spesa(tetto_spesa)
    