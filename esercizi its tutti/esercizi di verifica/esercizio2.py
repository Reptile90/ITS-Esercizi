'''La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.'''

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return len(numbers)
    else:
        return sum(numbers) / len(numbers)
    

numbers:list = list(range(201))
print(calculate_average(numbers))