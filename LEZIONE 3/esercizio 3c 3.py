'''Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta'''

oggetti:list =[]

for i in range(3):
    scelta:str = input("Inserisci un oggetto: ")
    oggetti.append(scelta)

match oggetti:
    case ["penna","matita", "quaderno"]:
        print("Categoria: Materiale scolastico")
    case ["sedia", "tavolo", "armadio"]:
        print("Categoria: Mobili")
    case ["pane", "latte", "uova"]:
        print("Categoria: Prodotti alimentari")
    case ["telefono", "computer", "tablet"]:
        print("Categoria: Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")