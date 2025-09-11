from string import ascii_lowercase

def vocali_consonanti(char)->str:
    char = char.lower()
    if char in "aeiou":
        return "Vocale"
    else:
        return "Consonante"
    
    
    
for char in ascii_lowercase:
    print(vocali_consonanti(char))    
