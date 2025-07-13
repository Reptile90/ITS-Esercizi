from Utente import Utente
from Url import Url

class VenditoreProf(Utente):
    def __init__(self, username, vetrina:Url):
        super().__init__(username)
    pass