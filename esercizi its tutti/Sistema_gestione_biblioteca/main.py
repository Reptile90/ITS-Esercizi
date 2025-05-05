


from Libro import Libro
from Biblioteca import Biblioteca

# Creiamo l'oggetto biblioteca
mia_biblioteca = Biblioteca()

# Aggiungiamo alcuni libri
print(mia_biblioteca.aggiungi_libro(Libro("1984", "George Orwell")))
print(mia_biblioteca.aggiungi_libro(Libro("Il Nome della Rosa", "Umberto Eco")))
print(mia_biblioteca.aggiungi_libro(Libro("I Promessi Sposi", "Alessandro Manzoni")))
print(mia_biblioteca.aggiungi_libro(Libro("Il Signore degli Anelli", "J.R.R. Tolkien")))

print("\n-- Libri disponibili inizialmente --")
print(mia_biblioteca.libri_disponibili())

# Prestiamo un libro
print("\n-- Prestito libro '1984' --")
print(mia_biblioteca.presta_libro("1984"))

# Proviamo a prestare di nuovo lo stesso libro (caso limite)
print("\n-- Tentativo di doppio prestito per '1984' --")
print(mia_biblioteca.presta_libro("1984"))

# Proviamo a prestare un libro che non esiste
print("\n-- Prestito libro inesistente 'Harry Potter' --")
print(mia_biblioteca.presta_libro("Harry Potter"))

# Mostriamo i libri disponibili dopo i prestiti
print("\n-- Libri disponibili dopo i prestiti --")
print(mia_biblioteca.libri_disponibili())

# Restituiamo un libro
print("\n-- Restituzione libro '1984' --")
print(mia_biblioteca.restituisci_libro("1984"))

# Proviamo a restituire di nuovo (caso limite)
print("\n-- Doppia restituzione libro '1984' --")
print(mia_biblioteca.restituisci_libro("1984"))

# Proviamo a restituire un libro inesistente
print("\n-- Restituzione libro inesistente 'Harry Potter' --")
print(mia_biblioteca.restituisci_libro("Harry Potter"))

# Mostriamo i libri disponibili dopo le restituzioni
print("\n-- Libri disponibili dopo le restituzioni --")
print(mia_biblioteca.libri_disponibili())

# Stato finale del catalogo
print("\n-- Stato finale dei libri in biblioteca --")
print(mia_biblioteca.mostra_stato_libri())