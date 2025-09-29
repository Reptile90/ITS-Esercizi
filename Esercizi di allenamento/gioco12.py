def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    seta=set(a)
    setb=set(b)
    
    l= list (seta.intersection(setb))
    
    return sorted(l)
    
    
    
    
    
    
a = [5, 3, 9, 1, 3, 7]
b = [4, 3, 7, 7, 2, 5]    
print(intersection_sorted(a,b))