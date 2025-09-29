def are_anagrams(a: str, b: str) -> bool:
    a = a.replace(" ","").lower()
    b = b.replace(" ","").lower()
    d1 = {}
    d2 = {}
    for char in a:
        if char in d1:
            d1[char] += 1
        else:
            d1[char] = 1
            
    for char in b:
        if char in d2:
            d2[char] += 1
        else:
            d2[char] = 1
            
    return d1 == d2
a = "Conclave dei Set"
b = "Set dei Conclave"

print(are_anagrams(a,b))