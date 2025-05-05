'''Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%'''

print('Per ciascun lancio della moneta inserisci "t" o "T" se è uscito "testa" mentre inserisci "c" o "C" se è uscito "croce".\n')

testa = 0
croce = 0

for i in range(1, 9):
    risultato = input(f"Lancio {i}: ").strip().lower()

    match risultato:
        case "t":
            testa += 1
        case "c":
            croce += 1
        case _:
            print("Valore non valido! Conta come croce per default.")
            croce += 1

totale = testa + croce
perc_testa = (testa / totale) * 100
perc_croce = (croce / totale) * 100

print(f"\nTotale \"testa\": {testa}")
print(f"Percentuale \"testa\": {perc_testa:.2f}%")

print(f"\nTotale \"croce\": {croce}")
print(f"Percentuale \"croce\": {perc_croce:.2f}%")
