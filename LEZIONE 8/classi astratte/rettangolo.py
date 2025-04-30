from forma_generica import FormaGenerica

class Rettangolo(FormaGenerica):

    #inizializzare un oggetto della classe rettangolo.
    def __init__(self):
        super().__init__()

        self.setShape("Rettangolo")

    def draw(self)->None:
        print(f"\n{self.getShape()}\n")

        #outer for
        for i in range(5):
            #inner for
            for j in range(5*2):

                #lato a e lato b del rettangolo
                if i == 0 or i == 5-1:
                    print("*", end=" ") #la funzione end= " " stiamo dicendo di stampare l'asterisco e lasciare uno spazio bianco invece che andare a capo

                #lato b e lato c del rettangolo
                elif j == 0 or j == 5*2-1:
                    print("*",end=" ")
                # spazi bianchi
                else:
                    print(" ",end=" ")
            print("\n", end="")