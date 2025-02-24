'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" 
(che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

parola ="" #definisco una variabile "parola" vuota

#inizio ciclo
while True:

#input dell'utente
    parola:str = str(input("Digita una parola o digita \"fine\" per uscire dal programma "))

#condizione di fine ciclo
    if parola == "fine":
        print("Programma Terminato")
        break

#confronto del carattere iniziale e finale
    if parola[0] == parola[-1]:
        print(f"La lettera iniziale e la lettera finale della parola \"{parola}\" sono uguali")

    else:
        print(f"La lettera iniziale e la lettera finale della parola \"{parola}\" sono diversi")




