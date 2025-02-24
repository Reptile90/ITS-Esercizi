'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.
Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******'''
#inizializzo una variabile contatore a 0  per le iterazioni e una variabile asterischi vuota
cont:int=0
asterischi:str = ""

#inizializzo il ciclo con la condizione che il contatore deve essere minore di 5 per avere 5 inserimenti
while cont < 5:
    
    #input utente
    numero:int= int(input("Inserisci un numero da 1 a 30: "))

    #condizione che verifica se il numero è compreso tra 1 e 30
    if 1 <= numero <= 30:

        #utilizzo il moltiplicatore di stringhe incrementando la variabile asterischi
        asterischi += "*" * numero + "\n"

        #incremento il contatore
        cont+=1
        
        #stampo uno spazio vuoto per farsi che il risultato non sia agganciato all'inserimento in ouput
        print()
    
    else:

        #stampo il messaggio di errore all'utente nel caso di numero non valido
        print("Numero errato, inserisci un numero valido")

#stampo la variabile asterischi dopo 5 iterazioni
print(asterischi)

    