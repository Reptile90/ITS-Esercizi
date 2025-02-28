'''Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.'''

lista_numeri:list[int] = []

for numero in range(1,1000001):
    lista_numeri.append(numero)

print(lista_numeri)
valore_min = min(lista_numeri)
valore_max = max(lista_numeri)

somma = sum(lista_numeri)

print(f"Minimo: {valore_min}")
print(f"Massimo: {valore_max}")
print(f"Somma totale: {somma}")
