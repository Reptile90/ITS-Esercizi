'''Un tamburo bronzeo batte ritmi di tre e cinque; il varco risponde alla loro somma: evoca `sum_multiples(limit)` per restituire la somma di tutti i numeri **minori di** `limit` divisibili per `3` **oppure** `5`. Se `limit` ≤ `0`, torna `0`. Mantieni la firma e soddisfa i test.'''

def sum_multiples(limit: int) -> int:
    somma = 0
    if limit <= 0:
        return 0
    else:
        for n in range (limit):
            if n % 3 == 0 or n % 5 == 0:
                somma += n
    return somma        



print(sum_multiples(93))