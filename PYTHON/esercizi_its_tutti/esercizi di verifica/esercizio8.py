'''Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.'''


def count_isolated(numeri:list) -> int:
    cont = 0
    num =len(numeri)
    for i in range(len(numeri)):
        if (i == 0 or numeri[i] != numeri[i-1]) and (i == num -1 or numeri[i] != numeri[i+1]):
            cont += 1
    return cont
    