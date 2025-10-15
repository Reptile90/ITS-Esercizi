'''Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista'''

def frequency_dict(elements: list) -> dict:
    frequency = {}
    for element in elements:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency


print(frequency_dict(['a', 'b', 'c', 'a', 'b', 'c', 'a']))