class Movie:
    
    def __init__(self, movie_id:str,title:str,director:str, is_rented = False):
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
        
    def rent(self)->None:
        if self.is_rented == False:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è già noleggiato")
    
    
    def return_movie(self)->None:
        if self.is_rented == True:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
            
            
class Customer:
    
    def __init__(self, customer_id:str, name:str):
        
        self.customer_id = customer_id
        self.name = name
        self.rented_movies:list[Movie]= []
        
    def rent_movie(self, movie: Movie):
        if movie in self.rented_movies:
            print(f"Il film '{movie.title}' è già stato noleggiato da questo cliente.")
        else:
            self.rented_movies.append(movie)
            
    def return_movie(self, movie:Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
            
            
class VideoRentalStore:
    
    def __init__(self):
        self.movies:dict[str,Movie]={}
        self.customers:dict[str,Customer]= {}
        
    def add_movie(self,movie_id:str, title:str,director:str)->None:
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id,title,director)
        else:
            print(f"Il film con ID '{movie_id}' esiste già.")
            
    def register_customer(self,customer_id:str,name:str)->None:
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id,name)
        else:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")
            
    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            if not movie.is_rented:
                customer.rent_movie(movie)
                movie.rent()
            else:
                print(f"Il film '{movie.title}' è già noleggiato.")
        else:
            print("Cliente o film non trovato.")

    def return_movie(self,customer_id:str, movie_id:str)->None:
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            if movie in customer.rented_movies:
                customer.return_movie(movie)
                movie.return_movie()
            else:
                print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
        else:
            print("Cliente o film non trovato.")
            
    def get_rented_movies(self,customer_id:str)->list[Movie]:
        
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            return customer.rented_movies
        else: 
            print("Cliente non trovato.")
            return []
        
        
if __name__ == "__main__":
    # Creazione di un nuovo videonoleggio
    videonoleggio = VideoRentalStore()

    # Aggiunta di nuovi film
    videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
    videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

    # Registrazione di nuovi clienti
    videonoleggio.register_customer("101", "Alice")
    videonoleggio.register_customer("102", "Bob")

    # Noleggio di film
    videonoleggio.rent_movie("101", "1")
    videonoleggio.rent_movie("102", "2")

    # Tentativo di noleggiare un film già noleggiato
    videonoleggio.rent_movie("101", "1")

    # Restituzione di film
    videonoleggio.return_movie("101", "1")

    # Tentativo di restituire un film non noleggiato
    videonoleggio.return_movie("101", "1")

    # Ottenere la lista dei film noleggiati da un cliente
    rented_movies_alice = videonoleggio.get_rented_movies("101")
    print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

    rented_movies_bob = videonoleggio.get_rented_movies("102")
    print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")
                
                    