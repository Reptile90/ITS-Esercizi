'''Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.

La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!'''


def integerPower(base, exp)-> int:
    if base > 0 and exp > 0:
        power = base ** exp
    else:
        print("Rrrore, non è possibile accettare numeri negativi")
    return power


print(integerPower(3, 4))
print(integerPower(2, 5))


