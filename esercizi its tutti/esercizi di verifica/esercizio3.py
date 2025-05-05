'''Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.'''

def remove_duplicates(lista_num) -> list:
    duplicates = set()
    newlist = []
    for element in lista_num:
        if element not in duplicates:
            duplicates.add(element)
            newlist.append(element)
    return newlist


print(remove_duplicates([1, 2, 3, 1, 2, 4]))