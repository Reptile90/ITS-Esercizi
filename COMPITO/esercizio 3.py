'''
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale. 
Il programma deve poi visualizzare la stringa ottenuta in output.
Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

#Input utente
string:str = input("Digita una parola: ")

#Creo una variabile vuota
reversed_string = ""

#Inizializzo il ciclo, dove ogni carattere viene aggiunto alla variabile vuota all'inizio
for char in string:

    reversed_string = char + reversed_string

#Stampa la stringa al contrario
print(f"La parola {string} al contrario diventa {reversed_string}")

    

