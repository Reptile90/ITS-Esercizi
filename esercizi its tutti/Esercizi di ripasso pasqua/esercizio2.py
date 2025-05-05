'''Scrivi una funzione che determina se un numero è 'magico'. 
Un numero è considerato magico se è divisibile per 4 ma non per 6.'''

def numero_magico(num: int) -> bool:
    if num % 4 == 0 and num % 6 != 0:
        return True
    else:
        return False
    



print(numero_magico(8))

print(numero_magico(12))