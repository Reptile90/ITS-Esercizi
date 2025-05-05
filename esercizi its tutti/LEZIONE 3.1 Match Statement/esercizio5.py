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


oggetti:list[str] = []

while len(oggetti) < 3:
    utente = input("Inserisci l'oggetto che vuoi aggiungere: ")
    oggetti.append(utente)

match oggetti:
    case ["penna", "matita", "quaderno"]:
        for oggetto in oggetti:
            print(f"Nome: {oggetto}\nCategoria: Materiale scolastico")
    case ["pane", "latte", "uova"]:
        for oggetto in oggetti:
            print(f"Nome: {oggetto}\nCategoria: Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        for oggetto in oggetti:
            print(f"Nome: {oggetto}\nCategoria: Mobili")
    case ["telefono", "computer", "tablet"]:
        for oggetto in oggetti:
            print(f"Nome: {oggetto}\nCategoria: Dispositivi elettronici")
    case _:
        for oggetto in oggetti:
            print(f"Nome: {oggetto}\nCategoria sconosciuta")


