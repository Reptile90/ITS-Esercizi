'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali).
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.
Il programma deve:
Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).'''

#definisco le variabili e il contatore
media:float = 0
somma:float = 0
max= float('-inf')
min= float('inf')
cont=0

#inizializzo il ciclo
while True:
    
    #input utente
    numero:float= float(input("Digita un numero reale non negativo: "))
    
    #condizione di chiusura del ciclo
    if numero <= 0:
        break
    
    #condizione per definire il numero più grande
    if numero > max:
        max = numero
    
    #condizione per definire il numero più piccolo
    elif numero < min:
        min = numero

    #verifica se il numero inserito è intero
    if numero.is_integer():
        somma += numero
        cont += 1

#concluso il ciclo calcola la media
if cont > 0:
    media=somma/cont

#stampa media, max e mix
print(f"La media dei numeri digitati è {media:.2f}")
print(f"Il numero più grande tra i numeri digitati è {max:.2f}")
print(f"il numero più piccolo tra i numeri digitati è {min:.2f}")
    
    



