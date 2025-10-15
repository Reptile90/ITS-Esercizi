'''L'ultima sala canta note ripetute: devi comprimerle senza perdere il motivo. Intona `rle(s)` per restituire la codifica run‑length come lista di tuple `(carattere, conteggio)` scorrendo `s`; se `s` è vuota, `[]`. Mantieni la firma e placa i test.'''

def rle(s: str) -> list[tuple[str,int]]:
    
    if not s:
        return []
    result = []
    corrente = s[0]
    count = 1
    for char in s[1:]:
        if char == corrente:
            count += 1
        else:
            result.append((corrente, count))
            corrente = char
            count = 1
    result.append((corrente, count))
    return result


print( rle("")) 
print( rle("a")) 
print( rle("aaabbcaaa")) 
print( rle("abcd"))