def recursiveCountdown(n:int)-> None:

    if n < 0:
        print("Error! Inserted number is negative!")
    elif n == 0:
        print(0)
    else:
        print(n)
        recursiveCountdown(n-1)



def recursiveSum(n:int)-> int:
    if n < 0:
        print("Errore, il numero è negativo")
        return 0
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n-1))
    


def recursiveSumInRange(a:int,b:int)->int:
    if a > b:
        temp:int = a
        a = b
        b = temp
    if b == a:
        return int(a)
    else:
        return int(b + recursiveSumInRange(a,b-1))

print(recursiveSumInRange(5,10))