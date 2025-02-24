'''Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0
Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''

#inizializzo le variabili somma_pari,somma_dispari, media, la lista dei numeri inseriti e un contatore necessario a calcolare la media
somma_pari:int=0
somma_dispari:int=0
media:float=0.0
lista_numeri:list[int] = []
cont:int=0

#inizializzo il ciclo
while True:

    #input utente
    numero:int = int(input("Inserisci un numero intero o inserisci il numero 0 per uscire: "))

    #condizione di uscita dal ciclo
    if numero == 0:
        break

    #ad ogni iterazione inserisco i numeri nella lista
    lista_numeri.append(numero)

#inizializzo un secondo ciclo che permette di verificare se i numeri sono pari e incrementare la somma degli stessi 
for n in lista_numeri:
    if n % 2 == 0:
        somma_pari += n
    
    #se i numeri sono dispari incremento la somma dei numeri dispari e incremento il contatore
    else:
        somma_dispari += n
        cont += 1
#condizione se il contatore è maggiore di zero faccio la media dei numeri dispari
if cont > 0:
    media = somma_dispari / cont

frequenze:dict[int] = {}
for n in lista_numeri:
    if n in frequenze:
        frequenze[n] += 1
    else:
        frequenze[n] = 1

max_frequenza = max(frequenze.values())
numeri_frequenti = []
for numero, freq in frequenze.items():
    if freq == max_frequenza:
        numeri_frequenti.append(numero)

print(f"La somma dei numeri pari è {somma_pari}")
print(f"La media dei numeri dispari è {media:.2f}")
print(f"I numeri più frequenti sono {', '.join(str(numero) for numero in numeri_frequenti)} e si ripetono {max_frequenza} volte")



