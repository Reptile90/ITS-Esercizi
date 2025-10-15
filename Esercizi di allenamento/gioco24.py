'''Le mura hanno incavi per gemme **prime**: devi elencarle tutte. Forja `primes_up_to(n)` per restituire la lista dei numeri primi **≤ n** in ordine crescente; se `n` < `2`, ritorna `[]`. Mantieni la firma e apri i test.'''

def primes_up_to(n: int) -> list[int]:
    
    if n < 2:
        return []
    
    lista_primi = []
    for numero in range(2, n + 1):  # include n
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                break
        else:
            lista_primi.append(numero)
    
    return lista_primi
    
    
print(primes_up_to(15))