def letter_count(text: str) -> dict[str,int]:
    d= {}
    text = text.strip("").lower()
    for char in text:
        if char.isalpha():
            if char in d:
                d[char]+= 1
            else:
                d[char]= 1
    return d
    
    
    
    
text = "Sussurri tra le foglie, 123! Luci & metallo."
print(letter_count(text))