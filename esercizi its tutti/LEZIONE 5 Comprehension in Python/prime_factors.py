def prime_factors(n:int) -> list[int]:    
    """
    Restituisce una lista dei fattori primi del numero intero positivo n.
    """
    ffattori = []
    divisore = 2
    while n > 1:
        while n % divisore == 0:
            ffattori.append(divisore)
            n = n // divisore
        divisore += 1
    return ffattori

print(prime_factors(60))