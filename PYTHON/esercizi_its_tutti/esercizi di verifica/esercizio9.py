'''Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.'''

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    newset1 = set({})
    newset2 = set({})

    for num in original_set:
        newset1.add(num)

    for num in elements_to_remove:
        newset1.add(num)

    for num in newset1:
        if num in elements_to_remove:
            newset2.add(num)

    return newset1.difference(newset2)

print(remove_elements({5, 6, 7}, [7, 8, 9]))