def puoi_arrivare(lista)->bool:
    max_position = 0
    for i in range(len(lista)):
        if i > max_position:
            return False
        max_position =max(max_position,i + lista[i])
    return True
        


print(puoi_arrivare([2, 3, 1, 1, 4])) 
print(puoi_arrivare([3, 2, 1, 0, 4])) 
print(puoi_arrivare([1, 1, 1, 1, 1])) 
print(puoi_arrivare([0]))