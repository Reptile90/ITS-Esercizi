class MovieCatalog:
    def __init__(self):
        self.movie_catalog = {}
    
    #metodo per aggiungere un film
    def add_movie(self,director_names:str,movies:list)->dict:
        if director_names not in self.movie_catalog:
            self.movie_catalog[director_names] = set()
        if isinstance(movies,str):
            movies = [movies]
        self.movie_catalog[director_names].update(movies)
        print(f"Aggiunti film per {director_names}: {movies}")

    #metodo per rimuovere un film
    def remove_movie(self, director_names:str, movie:str)->dict:
        if director_names not in self.movie_catalog:
            print(f"Regista {director_names} non trovato")
            return
        if movie in self.movie_catalog[director_names]:
            self.movie_catalog[director_names].remove(movie)
            print(f"Film '{movie}' rimosso da {director_names}.")
            if not self.movie_catalog[director_names]:
                del self.movie_catalog[director_names]
                print(f"Regista '{director_names}' rimosso dal catalogo.")
            else:
                print(f"Il film '{movie}' non è presente per il regista '{director_names}'.")
            return self.movie_catalog
        
    #metodo per visionare la lista dei registi
    def list_directors(self)->list:
        list_directors = list(self.movie_catalog.keys())
        return f"Lista registi: {', '.join(list_directors)}"
    
    #metodo per visionare i film di un determinato regista
    def get_movies_by_director(self,director_name)->list:
        if director_name in self.movie_catalog:
            print(f"Film di {director_name}:")
            for movie in self.movie_catalog[director_name]:
                print(f"- {movie}")
        else:
            print(f"Regista '{director_name}' non trovato nel catalogo.")

    #metodo per ricercare un film secondo un certo titolo
    def search_movies_by_title(self,title:str)->str:
        title= title.lower()
        search_result= {}
        for director,movies in self.movie_catalog.items():
            movie_match = []
            for movie in movies:
                if title in movie.lower():
                    movie_match.append(movie)
            if movie_match:
                search_result[director] = movie_match
        if search_result:
            print(f"Film trovati con la parola '{title}':")
            for director, matched_movies in search_result.items():
                print(f"{director}:")
                for movie in matched_movies:
                    print(f"  - {movie}")
        else:
            print(f"Il film {title} non è stato trovato")



def main():
    catalog = MovieCatalog()

    while True:
        print("\n--- MENU GESTIONE CATALOGO FILM ---")
        print("1. Aggiungi film")
        print("2. Rimuovi film")
        print("3. Elenca registi")
        print("4. Mostra film di un regista")
        print("5. Cerca film per titolo")
        print("6. Esci")
        choice = input("Scegli un'opzione (1-6): ")

        if choice == "1":
            director = input("Nome del regista: ")
            movies_input = input("Inserisci uno o più film separati da virgola: ")
            movies = [m.strip() for m in movies_input.split(",")]
            catalog.add_movie(director, movies)

        elif choice == "2":
            director = input("Nome del regista: ")
            movie = input("Nome del film da rimuovere: ")
            catalog.remove_movie(director, movie)

        elif choice == "3":
            print(catalog.list_directors())

        elif choice == "4":
            director = input("Nome del regista: ")
            catalog.get_movies_by_director(director)

        elif choice == "5":
            title = input("Parola chiave nel titolo: ")
            catalog.search_movies_by_title(title)

        elif choice == "6":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()













