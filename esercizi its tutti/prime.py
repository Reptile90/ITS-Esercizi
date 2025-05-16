def prime(n:int)->bool:

    if (str(n)[-1] == "0" or str(n)[-1]) == "5" and n != 5:

        return False
    for i in range(2, (n//2) + 1 ):
        if n % i == 0:
            print(f"divisore trovato {i}")
            return False
    return True



print(prime(77676876865865874))