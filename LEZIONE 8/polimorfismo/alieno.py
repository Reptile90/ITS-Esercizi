class Alieno:
    '''
    di un alieno ci serve sapere la galassia di provenienza
    
    '''
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)

    #inizializzare un oggetto della classe alieno
    def setGalaxy(self,galaxy:str)->None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia di provenienza non deve essere una stringa vuota")
    
    def getGalaxy(self)->str:
        return self.galaxy
    
    def __str__(self)->str:
        return f"\nAlieno proveniente dalla galassia {self.galaxy}"
    def speak(self)->None:
        print(f"inasdmnfosmd")
