def baricentro(v: list[int])->str|bool:
    
    
    for i in range(len(v)):
        if sum(v[:i+1]) == sum(v[i+1:]):
            return 
        
    return None
            
def printResult(v: list[int])->str:
    if baricentro(v):
        return f"Esiste il baricentro del vettore v={v} ed è dato dall'indice i={baricentro(v)}"
    else:
        return f"Il baricentro del vettore v={v} non esiste!"

        
def baricentroOttimizzato(v: list[int]):
    tot=0
    left_sum=0
    
    for num in v:
        
        tot+= num
    
    for i in range(len(v)):
        left_sum += v[i]
        if tot - left_sum == left_sum:
            
            return i
    return None
        



if __name__ == "__main__":

    v1 = [1, 2, 3, 2, 5, 2, 1]
    print(baricentro(v1))

    v2 = [2, 0, -1, 4, 6, 3, -1]
    print(baricentro(v2))

    print(printResult(v1))

    print(printResult(v2))

    print(baricentroOttimizzato(v1))
    print(baricentroOttimizzato(v2))