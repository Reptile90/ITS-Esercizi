import re

def is_valid_name(name):
    return bool(re.match(r"^[A-Z][a-z]{2,}$", name))



print(is_valid_name("Marco"))  # True
print(is_valid_name("marco"))  # False
print(is_valid_name("Ma"))     # False
