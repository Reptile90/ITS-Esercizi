'''Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valore'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    conteggio:dict[int:int] = da_rimuovere.copy()
    risultato:list[int]= []
    for elemento in lista:
        if elemento in da_rimuovere and conteggio[elemento] > 0:
            conteggio[elemento] -= 1
        else:
            risultato.append(elemento)
    
    return risultato
            
                    





print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1})) 