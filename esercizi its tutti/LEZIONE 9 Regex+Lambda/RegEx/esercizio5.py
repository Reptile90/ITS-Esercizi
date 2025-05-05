import re

def find_dates(text):
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
print(find_dates(text))