''' Uso con filter()
Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. Usa filter() con una lambda per ottenere solo i numeri pari.'''

nums = [5, 12, 17, 18, 24, 32]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)