def even_odd_pattern(numbers: list[int]) -> list[int]:
    """
    Riordina la lista in modo che tutti i numeri pari vengano prima dei numeri dispari.
    L'ordine relativo tra i numeri non è necessariamente mantenuto.
    """
    even:list[int] = []  # Lista per i numeri pari
    odd:list[int] = []   # Lista per i numeri dispari

    # Separa numeri pari e dispari
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    # Combina le due liste: prima i pari, poi i dispari
    return even + odd

# Test case
print(even_odd_pattern([3, 1, 2, 4]))  # Output: [2, 4, 3, 1]
