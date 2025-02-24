'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

#inizializzo la lista a e b
lista_a:list[int] = [23, 48, 92, 104, 24 ]
lista_b:list[int] = [84, 12, 36, 85, 91]

# inizializzo una lista c vuota dove andrà il risultato delle somme
lista_c:list[int] = []

#creo una variabile somma vuota
somma:int=0

#inizializzo il ciclo for per scorrere l'indice
for i in range(len(lista_a)):

    #effettuo la somma della lista a partire dall'indice 0 + l'indice della lunghezza della lista -1 - l'indice
    somma = lista_a[i] + lista_b[len(lista_a)-1 - i]

    #inserisco il risultato delle somme nella variabile lista c

    lista_c.append(somma)
    
#stampo le liste a,b e c
print(lista_a)
print(lista_b)
print(lista_c)



