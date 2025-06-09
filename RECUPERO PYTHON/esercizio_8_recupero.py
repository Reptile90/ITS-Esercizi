class Movie:
    def __init__(self, movie_id:str,  title:str, director:str)->None:
        self.movie_id:str = movie_id
        self.title:str = title
        self.director:str = director
        self.is_rented:bool = False

    
    def rent(self)->None:
        if not self.is_rented:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è già noleggiato")
            

    def return_movie(self)->None:
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")



class Customer:
    def __init__(self,customer_id:str, name:str, rented_movies:list[Movie]= [])->None:
        self.customer_id:str = customer_id
        self.name:str = name
        self.rented_movies:list[Movie] = rented_movies

    def rent_movie(self, movie: Movie) -> None:
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato")
        
    def return_movie(self, movie: Movie) -> None:
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente")
        

class VideoRentalStore:
    def __init__(self, movies:dict[str,Movie]={}, customers:dict[str,Customer]={})->None:
        self.movies:dict[str,Movie] = movies
        self.customers:dict[str,Customer] = customers
    

    def add_movie(self,movie_id:str,title:str,director:str)->None:
        if movie_id not in self.movies:
            movie:Movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie
        else:
            print(f"Il film con ID '{movie_id} esiste già")
        
    def register_customer(self, customer_id:str,name:str)->None:
        if customer_id not in self.customers:
            customer:Customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
        else:
            print(f"Il cliente con ID '{customer_id} è già registrato")
        
    def rent_movie(self,customer_id:str, movie_id:str)->None:
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def return_movie(self,customer_id:str, movie_id:str)->None:
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self,customer_id:str)->list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato")
            return []
    def get_rented_movies_all(self)->list[Movie]:
        list_rented:list[Movie]=[]
        for customer in self.customers.values():
            list_rented.extend(customer.rented_movies)
        return list_rented

if __name__ == "__main__":
    store = VideoRentalStore({}, {})

    
    store.add_movie("M001", "Inception", "Christopher Nolan")
    store.add_movie("M002", "Interstellar", "Christopher Nolan")


    store.register_customer("C001", "Mario Rossi")


    store.rent_movie("C001", "M001")
    store.rent_movie("C001", "M002")


    store.rent_movie("C001", "M001")


    print("Film noleggiati da Mario Rossi:")
    for movie in store.get_rented_movies("C001"):
        print(f"- {movie.title} ({movie.director})")

    store.return_movie("C001", "M001")

    store.return_movie("C001", "M001")

    print("\nFilm ancora noleggiati da Mario Rossi:")
    for movie in store.get_rented_movies("C001"):
        print(f"- {movie.title}")

    print(store.get_rented_movies_all())