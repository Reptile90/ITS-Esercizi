import re

def mask_numbers(text):
    return re.sub(r"\d+", "###", text)

text = "Il codice è 12345 e la data è 2025."
print(mask_numbers(text))