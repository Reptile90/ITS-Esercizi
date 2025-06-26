
import random

class Creatura:
    __nome:str

    def __init__(self, nome:str) -> None:
        self.setNome(nome)

    def setNome(self,nome:str)->None:
        if isinstance(nome,str):
            self.__nome:str = nome
        else:
            self.__nome:str = "Creatura generica"
    
    def getNome(self)->str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.__nome}"
    


class Alieno(Creatura):
    _matricola:int
    _munizioni:list[int]

    def __init__(self, nome: str) -> None:
        self.__setMatricola()
        if nome != "Robot":
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!')
        
        super().__init__(f"Robot-{self.getMatricola()}")

        self.__setMunizioni()

    
    def __setMatricola(self)->None:
        self.__matricola:int = random.randint(10000,90001)

    def getMatricola(self)->int:
        return self.__matricola

    def __setMunizioni(self)->None:
        self.__munizioni = [n**2 for n in range(16)]

    def getMunizioni(self)->list[int]:
        return self.__munizioni
    
    

    def __str__(self) -> str:
        return f"Alieno: {self.getNome()}"


class Mostro(Creatura):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.__setAssalto()
        self.__setVittoria("GRAAAHHH ")
        self.__setSconfitta("Uuurghhh ")
    
    def __setAssalto(self)->None:
        self.__assalto = [random.randint(1,100) for n in range(16) ]
    
    def getAssalto(self)->list[int]:
        return self.__assalto

    def __setVittoria(self, vittoria:str)->None:
        if isinstance(vittoria,str):
            self.__urlo_vittoria = vittoria
        else:
            self.__urlo_vittoria = "GRAAAHHH "

    def getVittoria(self)->str:
        return self.__urlo_vittoria


    def __setSconfitta(self, sconfitta:str)->None:
        if isinstance(sconfitta, str):
            self.__gemito_sconfitta = sconfitta
        else:
            self.__gemito_sconfitta = "Uuurghhh "

    def getSconfitta(self)->str:
        return self.__gemito_sconfitta

    def __str__(self) -> str:
        nome = self.getNome()
        nome_mostro:str= ""
        for i in range(len(self.getNome())):
            if i % 2 == 0:
                nome_mostro += self.getNome()[i].lower()
            else:
                nome_mostro += self.getNome()[i].upper()

        return f"Mostro: {nome_mostro}"
    


def pariUguali(a: list[int], b: list[int])->list[int]:
    c:list = []

    i = 0
    while i < len(a) and i < len(b):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
        i += 1
    return c

def combattimento(a: Alieno, m: Mostro)->str|None:
    
    if not isinstance(a,Alieno) or not isinstance(m,Mostro):
        print("Combattimento interrotto")
        return None
    else:
        munizioni_alieno = a.getMunizioni()
        assalto_mostro = m.getAssalto()
        lista_vittoria = pariUguali(munizioni_alieno,assalto_mostro)
        conteggio_vittoria= 0

    
        for element in lista_vittoria:
            if element == 1:
                conteggio_vittoria += 1
        if conteggio_vittoria == 4:
            return f"\n{m.getVittoria()}" * 3
        else:
            return m.getSconfitta()
        
def proclamaVincitore(c:Creatura):
    vincitore = c.__str__()
    altezza = 5
    lunghezza = len(vincitore) + 10

    print("*" * lunghezza)

    for i in range(altezza):
        if i == altezza // 2:
            print("* ", end="")
            print(vincitore, end= "")
            print("       *")
        else:
            print("*" + " " * (lunghezza - 2) + "*")
    print("*" * lunghezza)

        
if __name__ == "__main__":

    garrus:Alieno = Alieno("Garrus")
    print(f"Creato {garrus}")
    print(f"Munizioni dell'alieno: {garrus.getMunizioni()}")

    krogan:Mostro = Mostro("Krogan")
    print(f"Creato {krogan}")
    print(f"Valori di assalto del Krogan: {krogan.getAssalto()}")


    print("\n-----Inizio Combattimento-----")
    
    esito = combattimento(garrus,krogan)

    print(f"\nEsito del combattimento:\n{esito}")

    if esito == krogan.getSconfitta():
        print(f"\nGli alieni hanno vinto!\n")
        proclamaVincitore(garrus)
    else:
        print(f"\nI Mostri hanno vinto!\n")
        proclamaVincitore(krogan)

    
    

