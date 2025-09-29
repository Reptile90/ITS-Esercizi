def chunk(lst: list[int], size: int) -> list[list[int]]:
    
    if size <= 0:
        raise ValueError("size must be greater than 0")
    
    newlist = []
    cont1 = 0
    while cont1 < len(lst):
        lista = []
        cont2 = 0
        while cont2 < size and cont1 + cont2 < len(lst):
            lista.append(lst[cont1 + cont2])
            cont2 += 1
        newlist.append(lista)
        cont1 += size
    return newlist

        
        
            
            
    
    
    
    
    
    
lst = [1,2,3,4,5,6,7,8,9] 
size= 3
    
print(chunk(lst,size))