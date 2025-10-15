import re

def is_valid_cap(cap):
    return bool(re.match(r"^\d{5}$", cap))


print(is_valid_cap("70124"))  # True
print(is_valid_cap("A0123"))  # False
print(is_valid_cap("123456")) # False