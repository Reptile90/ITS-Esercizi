def range_sum(n: int) -> int:
    somma = 0
    if n == 0:
        return 0
    elif n <= 0:
        return 0
    else:
        for num in range(1,n+1):
            somma += num
    return somma



print(range_sum(9))