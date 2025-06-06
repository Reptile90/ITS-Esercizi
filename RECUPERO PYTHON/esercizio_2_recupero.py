'''Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.ù
'''

def positive_negative(number_list:int)->dict:

    positive:list[int] = []
    negative:list[int] = []
    dictionary:dict[list[int]] = {}

    for numero in number_list:
        if numero > 0:
            positive.append(numero)
        else:
            negative.append(numero)
    dictionary["Positivo"] = positive
    dictionary["Negativo"] = negative

    return dictionary


lista_numeri:list[int] = [1,3,-4,6,-89,90,-3,23,14,-45]
print(positive_negative(lista_numeri))