'''Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.'''

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    risultato_voti:dict[str:list[int]] = {}

    for elemento in voti:
        nome_studente = elemento["nome"]
        voti_studente = elemento["voto"]
        if nome_studente in risultato_voti:
            risultato_voti[nome_studente].append(voti_studente)
        else:
            risultato_voti[nome_studente] = [voti_studente]

    return risultato_voti




print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))


print(aggrega_voti([])) 