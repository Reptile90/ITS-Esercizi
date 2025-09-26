from Film import Film
from movie_genre import Azione,Commedia,Drama
from Noleggio import Noleggio


    
film_list = [
Azione(1, "Mad Max"),
Azione(2, "John Wick"),
Azione(3, "Die Hard"),
Azione(4, "Gladiator"),
Azione(5, "The Raid"),
Commedia(6, "The Mask"),
Commedia(7, "Superbad"),
Commedia(8, "Yes Man"),
Commedia(9, "The Intern"),
Drama(10, "The Shawshank Redemption")
]


noleggio:Noleggio = Noleggio(film_list)

print("Quale film vuoi noleggiare?")

cliente1 = 101
film1 = film_list[2]
noleggio.rentAMovie(film1,cliente1)

film2= film_list[6]
noleggio.rentAMovie(film2,cliente1)

cliente2 = 202
noleggio.rentAMovie(film2,cliente2)

film3 = film_list[7]
noleggio.rentAMovie(film3,cliente2)

noleggio.giveBack(film2,cliente1, giorniRitardo=2)

print("Film disponibili in negozio:")
noleggio.printMovies()
    
    
    