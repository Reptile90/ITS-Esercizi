class Contatore:
    def __init__(self):
        self.cont:int = 0

    def setZero(self)->int:
        self.cont = 0
        return self.cont

    def add1(self)->int:
        self.cont += 1
        return self.cont
    
    def sub1(self)->int:
        
        if self.cont == 0:
            print("Non è possibile eseguire la sottrazione")
        else:

            self.cont -= 1
        return self.cont
    
    def get(self)->int:
        return self.cont
    
    def mostra(self)->str:
        print(f"Conteggio attuale: {self.cont}")



 	

c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
z  = c.get()
print(z)