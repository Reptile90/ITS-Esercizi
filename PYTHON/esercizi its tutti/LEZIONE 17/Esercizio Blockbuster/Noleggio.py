from movie_genre import Azione,Commedia,Drama
class Noleggio:
    def __init__(self, film_list:list[Azione|Commedia|Drama])->None:
        self.film_list:list[Azione|Commedia|Drama] = film_list
        self.rented_film:dict[int,list[Azione|Commedia|Drama]] = {}
        
    def isAvailable(self, film: Azione | Commedia | Drama) -> bool:
        for movie in self.film_list:
            if movie.isEqual(film):
                print(f"Il film scelto è disponibile: {movie.getTitle()}")
                return True
        print(f"Il film scelto non è disponibile: {film.getTitle()}")
        return False

            
    def rentAMovie(self,film:Azione|Commedia|Drama, clientID:int)->str:
        if self.isAvailable(film):
            self.film_list.remove(film)
            self.rented_film[clientID]=[film]
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}")
        else:
            print(f"Non è possibile noleggiare il film{film.getTitle()}")
            
    def giveBack(self, film: Azione | Commedia | Drama, clientID: int, giorniRitardo: int) -> str:
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            if not self.rented_film[clientID]:
                del self.rented_film[clientID]
            self.film_list.append(film)
            totale = film.calcolaPenaleRitardo(giorniRitardo)
            print(f"Cliente: {clientID} La penale da pagare per il film {film.getTitle()} è di {totale} euro!")
        else:
            print(f"Il film {film.getTitle()} non risulta noleggiato dal cliente {clientID}")

                
                
    def printMovies(self)->str:
        for movie in self.film_list:
            print(f"{movie.getTitle()}-{movie.getGenere()}")
            
            
    def printRentMovies(self, clientID: int):
        if clientID in self.rented_film:
            print(f"Film noleggiati dal cliente {clientID}:")
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenere()}")
        else:
            print(f"Nessun film noleggiato dal cliente {clientID}")

            
            
    
        