def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    seta = set(a)
    setb = set(b)
    
    l= list(seta.symmetric_difference(setb))
    return sorted(l)
    
    
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]
print(symdiff_sorted(a,b))