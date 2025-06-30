'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
'''


def tuple_converter(tuple_list:list[tuple])->dict:
    dictionary:dict = {}

    for key,value in tuple_list:
        if key in dictionary:
            dictionary[key] += value
        else:
            dictionary[key] = value


    return dictionary



print(tuple_converter([("nome", "Stefano"), ("Cognome", "Reali")]))