'''Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.'''


giorno = int(input("Inserisci il giorno: "))
mese = int(input("Inserisci il mese: "))


data = (giorno, mese)


match data:
    case (1, 1):
        print("Il 1/1 è Capodanno!")
    case (14, 2):
        print("Il 14/2 è San Valentino!")
    case (2, 6):
        print("Il 2/6 è Festa della Repubblica Italiana!")
    case (15, 8):
        print("Il 15/8 è Ferragosto!")
    case (31, 10):
        print("Il 31/10 è Halloween!")
    case (25, 12):
        print("Il 25/12 è Natale!")
    case _:
        print(f"Nessuna festività importante in questa data.")