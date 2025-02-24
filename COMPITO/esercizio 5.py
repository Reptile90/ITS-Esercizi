'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

    Acquisisca in input un valore N (numero di euro disponibili).
    Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
    Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''


#inizializzo le variabili
barretta:int = 0

buono_sconto:int = 0

costo_barretta:int = 1

#inizializzo il primo ciclo per far inserire l'importo e incrementare il numero di barrette e buoni sconto
while True:
    n:int = int(input("Digita l'importo disponibile: "))
    if n == 0:
        print("Importo Insufficiente")
        break
    barretta += n // costo_barretta
    buono_sconto += n // costo_barretta

    #inizializzo il secondo ciclo per verificare quante barrette totali e quanti buoni sconto rimangono
    while buono_sconto >= 6:
        barretta_omaggio:int = buono_sconto // 6
        barretta += barretta_omaggio
        buono_sconto = buono_sconto % 6
    #stampo il risultato
    print(f"Hai acquistato {barretta} barrette")
    print(f"I buoni sconto rimanenti {buono_sconto}")



  
  
  




