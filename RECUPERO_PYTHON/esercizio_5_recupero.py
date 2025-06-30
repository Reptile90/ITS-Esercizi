'''Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.'''



def multiplier(numbers:list[int])->int:

    threshold = 60
    multiplier_num = 1

    for number in numbers:
        if number < threshold:
            multiplier_num *= number
        else:
            continue

    return multiplier_num


lista_numeri = [2, 34, 56, 70, 90, 140, 69, 60, 908, 34, 2, 59]
print(multiplier(lista_numeri))
