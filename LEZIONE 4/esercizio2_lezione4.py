'''Crea una funzione che generi un numero casuale all'interno di un intervallo specificato dall'utente.
Chiedi all'utente di indovinare il numero entro un numero massimo di tentativi specificato.
Fornisci un feedback all'utente dopo ogni tentativo, indicando se il suo tentativo è troppo alto, troppo basso o corretto.
Termina il ciclo quando l'utente indovina correttamente il numero o raggiunge il numero massimo di tentativi.
'''
from random import randint

def indovinaNumero(scelta:int):
    random_number:int = randint(1,scelta)
    tentativi:int = 0
    while tentativi < 4:
        numero_scelto = int(input(f"Indovina il numero (Tentativo {tentativi + 1}/4): "))
        if numero_scelto > random_number:
            print(f"Il numero {numero_scelto} è troppo alto")
        elif numero_scelto < random_number:
            print(f"Il numero {numero_scelto} è troppo basso")
        elif numero_scelto == random_number:
            print(f"Il numero {numero_scelto} è corretto, Hai vinto!")
            return
        else:
            print("Numero non accettato")
            
        tentativi += 1
    print(f" Hai perso! Il numero era il {random_number}")

scelta:int = int(input("Inserisci un numero maggiore di 1: "))

while True:
    if scelta > 1:
        print("Scelta accettata")
        break
    else:
        print("Scelta non valida. Ritenta")

indovinaNumero(scelta)