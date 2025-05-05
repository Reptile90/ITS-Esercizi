'''Scrivere un programma in Python che chieda all'utente di inserire il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.

Expected Output:

Inserire nome: Luca
Inserire gender. Digitare m per maschio e f per femmina: m
Nome: Luca
Gender: Maschio

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Inserire nome: Anna
Inserire gender. Digitare m per maschio e f per femmina: f
Nome: Anna
Gender: Femmina

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Inserire nome: Alex
Inserire gender. Digitare m per maschio e f per femmina: x
Mi dispiace Alex, non e' possibile procedere con la generazione di un documento di identità!'''


nome_input: str = input("Inserisci il tuo nome: ")
genere_input: str = input("Inserisci 'm' per maschio, 'f' per femmina: ")

nome_corretto: str = nome_input.title()
genere_completo: str | None = None

match genere_input.lower():
    case "m":
        genere_completo = "Maschio"
        print(f"Nome: {nome_corretto}\nGenere: {genere_completo}")
    case "f":
        genere_completo = "Femmina"
        print(f"Nome: {nome_corretto}\nGenere: {genere_completo}")
    case _:
        print(f"Mi dispiace {nome_corretto}, l'input per il genere ('{genere_input}') non è valido. Inserire 'm' o 'f'.")



