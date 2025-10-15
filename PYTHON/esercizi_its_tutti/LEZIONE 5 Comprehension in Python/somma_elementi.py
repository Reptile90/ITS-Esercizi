def somma_elementi(x:list[int], y:list[int]) -> list[int]:
    """
    Restituisce una lista risultante dalla somma elemento per elemento delle due liste x e y.
    Si assume che le due liste abbiano la stessa lunghezza.
    """
    result:list[int] = []
    for i in range(len(x)):
        result.append(x[i] + y[i])  # Somma i valori corrispondenti e li aggiunge alla lista risultato
    return result

# Test case
print(somma_elementi([1, 2, 3], [4, 5, 6]))  # Output: [5, 7, 9]
