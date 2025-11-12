'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

'''


def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    d = {}
    for key,value in tuples:
        if key not in d:
            d[key]= [value]
        else:
            d[key].append(value)
    return d



tuples = [(1,2),(4,2),(1,6),(9,3)]

print(lista_a_dizionario(tuples))

print(lista_a_dizionario([('c', 1), ('b', 2), ('c', 3), ('c', 4)]))

	

