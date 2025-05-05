'''Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.'''



animale = input("Digita il nome di un animale: ").strip().lower()
habitat = input(f"Digita l'habitat in cui vive l'animale {animale}: ").strip().lower()


animal_type = ""

match animale:
    case "cane" | "gatto" | "cavallo" | "elefante" | "leone" | "balena" | "delfino":
        animal_type = "mammifero"
        print(f"{animale.capitalize()} appartiene alla categoria dei Mammiferi!")
    case "serpente" | "lucertola" | "tartaruga" | "coccodrillo":
        animal_type = "rettile"
        print(f"{animale.capitalize()} appartiene alla categoria dei Rettili!")
    case "aquila" | "pappagallo" | "gufo" | "falco" | "cigno" | "anatra" | "gallina" | "tacchino":
        animal_type = "uccello"
        print(f"{animale.capitalize()} appartiene alla categoria degli Uccelli!")
    case "squalo" | "trota" | "salmone" | "carpa":
        animal_type = "pesce"
        print(f"{animale.capitalize()} appartiene alla categoria dei Pesci!")
    case _:
        animal_type = "sconosciuto"
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")


scheda_animale = {
    "nome": animale,
    "categoria": animal_type,
    "habitat": habitat
}


match (animal_type, habitat):

    case ("mammifero", "terra") if animale in ["cane", "gatto", "cavallo", "elefante", "leone"]:
        print(f"L'animale {animale} è uno dei mammiferi che può vivere sulla terra!")
    case ("mammifero", "acqua") if animale in ["balena", "delfino"]:
        print(f"L'animale {animale} è uno dei mammiferi che può vivere in acqua!")

    case ("rettile", "terra") if animale in ["serpente", "lucertola", "coccodrillo"]:
        print(f"L'animale {animale} è uno dei rettili che può vivere sulla terra!")
    case ("rettile", "acqua") if animale in ["tartaruga", "coccodrillo"]:
        print(f"L'animale {animale} è uno dei rettili che può vivere in acqua!")

    case ("uccello", "aria") if animale in ["aquila", "pappagallo", "gufo", "falco"]:
        print(f"L'animale {animale} è uno degli uccelli che può vivere in aria!")
    case ("uccello", "terra") if animale in ["gallina", "tacchino", "anatra"]:
        print(f"L'animale {animale} è uno degli uccelli che può vivere sulla terra!")
    case ("uccello", "acqua") if animale in ["cigno", "anatra"]:
        print(f"L'animale {animale} è uno degli uccelli che può vivere in acqua!")

    case ("pesce", "acqua"):
        print(f"L'animale {animale} è uno dei pesci che può vivere in acqua!")

    case ("mammifero" | "rettile" | "uccello" | "pesce", _):
        print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")

    case  _:
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}.")