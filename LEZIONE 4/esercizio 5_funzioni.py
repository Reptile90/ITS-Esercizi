'''Sistema di Gestione Inventario:

Crea una funzione che definisce un articolo con un codice, nome, quantità e prezzo.

Crea un database o dizionario per memorizzare gli articoli nell'inventario.

Implementa funzioni per aggiungere, rimuovere, cercare e aggiornare articoli nell'inventario.

Usa cicli for e istruzioni condizionali per gestire le varie operazioni dell'inventario.'''


def nuovoArticolo(codice: str, nome: str, quantita: int, prezzo: float) -> dict:
    return {
        "Codice": codice,
        "Nome": nome,
        "Quantità": quantita,
        "Prezzo": prezzo
    }

inventario: dict = {}

def aggiungiArticolo(codice: str, nome: str, quantita: int, prezzo: float) -> None:
    if codice in inventario:
        print("Articolo già presente, usa la funzione 'modificaArticolo' per modificarlo")
    else:
        inventario[codice] = nuovoArticolo(codice, nome, quantita, prezzo)
        print(f"Articolo {nome} aggiunto correttamente all'inventario")

def rimuoviArticolo(codice: str) -> None:
    if codice in inventario:
        nome = inventario[codice]["Nome"]
        del inventario[codice]
        print(f"Articolo {nome} (codice: {codice}) rimosso correttamente")
    else:
        print(f"Articolo con codice {codice} non presente.")

def cercaArticolo(codice: str) -> None:
    articolo = inventario.get(codice)
    if articolo:
        print("\nDettagli articolo:")
        for key, value in articolo.items():
            print(f"{key}: {value}")
    else:
        print(f"\nArticolo con codice {codice} non trovato.")

def modificaArticolo(codice: str, nome: str = None, quantita: int = None, prezzo: float = None) -> None:
    if codice in inventario:
        articolo = inventario[codice]
        if nome is not None:
            articolo["Nome"] = nome
        if quantita is not None:
            articolo["Quantità"] = quantita
        if prezzo is not None:
            articolo["Prezzo"] = prezzo
        print(f"Articolo {articolo['Nome']} modificato")
    else:
        print(f"Articolo con codice {codice} non trovato")

def visualizzaInventario() -> None:
    if not inventario:
        print("L'inventario è vuoto")
        return
    
    print("\nInventario attuale:")
    for codice, articolo in inventario.items():
        print(f"\nCodice: {codice}")
        for key, value in articolo.items():
            if key != "Codice":  # Evitiamo di ripetere il codice
                print(f"{key}: {value}")
    print()


aggiungiArticolo("C00024","Samsung Galaxy S25", 1, 1699)
aggiungiArticolo("C00042", "Iphone 16 Pro +" , 2, 1799)
aggiungiArticolo("D0001", "Laptop Asus Rouge", 4, 2400)

visualizzaInventario()

cercaArticolo("C00042")

modificaArticolo("C00042", "Iphone 16 Pro", 2, 1599)

visualizzaInventario()

rimuoviArticolo("D0001")

visualizzaInventario()