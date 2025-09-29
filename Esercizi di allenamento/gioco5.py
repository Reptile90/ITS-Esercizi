def flatten_once(nested: list[list[int]]) -> list[int]:
    newlist = []
    if len(nested) == 0:
        return nested
    for lst in nested:
        for num in lst:
            newlist.append(num)
            
    return newlist
    
    
    
    
    
    
    
    
lista = [[1,2,3,34],[2,23,52,13],[4,2,3,1]]
print(flatten_once(lista))