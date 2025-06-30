from __future__ import annotations
class Frazione:
    __numeratore:int
    __denominatore:int
    
    def set_numeratore(self,numeratore)->None:
        if isinstance(numeratore,int):
            self.__numeratore = numeratore
        else:
            self.__numeratore = 13

    def set_denominatore(self, denominatore)->None:
        if isinstance(denominatore, int) and denominatore != 0:
            self.__denominatore = denominatore
        else:
            self.__denominatore = 5

    def get_numeratore(self)->int:
        return self.__numeratore
    
    def get_denominatore(self)->int:
        return self.__denominatore
    
    def __init__(self, numeratore:int, denominatore:int):
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)
        

    def __str__(self):
        return f"{self.__numeratore}/{self.__denominatore}"
    
    def value(self):
        result = self.__numeratore / self.__denominatore
        return round(result, 3)
    
    def mcd(self,x:int,y:int)->int:
        if x < y:
            x, y = y, x
        mcd = 1
        for n in range(1, y + 1):
            if x % n == 0 and y % n == 0:
                mcd = n
        return mcd

    def semplifica_frazione(self):
        divisore = self.mcd(self.__numeratore,self.__denominatore)
        nuovo_numeratore = self.__numeratore // divisore
        nuovo_denominatore = self.__denominatore //divisore
        return Frazione(nuovo_numeratore,nuovo_denominatore)
    
    @staticmethod
    def semplifica(lista_frazioni: list[Frazione]) -> list[Frazione]:
        irriducibili = []
        for frazione in lista_frazioni:
            frazione_semplificate = frazione.semplifica_frazione()
            irriducibili.append(frazione_semplificate)
        return irriducibili
    
    @staticmethod
    def fraction_compare(lista_frazioni:list[Frazione], irriducibili:list[Frazione]):
        for i in range(len(lista_frazioni)):
            originale = lista_frazioni[i]
            semplificata = irriducibili[i]

            valore_originale = originale.value()
            valore_semplificato = semplificata.value()

            if valore_originale == valore_semplificato:
                print(f"La frazione {originale} = {valore_originale} è uguale alla semplificata {semplificata} = {valore_semplificato}")
            else:
                print(f" ERRORE: {originale} = {valore_originale} ≠ {semplificata} = {valore_semplificato}")

if __name__ == "__main__":
    l = [
        Frazione(1, 2),
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(12, 36),
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15)
    ]

    l_s = Frazione.semplifica(l)

    for f in l_s:
        print(f)

    Frazione.fraction_compare(l,l_s)
        


        