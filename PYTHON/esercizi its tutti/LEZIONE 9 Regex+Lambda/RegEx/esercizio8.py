import re

def find_codes(text):
    return re.findall(r"\b[A-Z0-9]{8}\b", text)



text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
print(find_codes(text)) 