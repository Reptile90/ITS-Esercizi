import re

def is_integer(s)->bool:
    return bool(re.fullmatch(r"-?\d+", s))     






print(is_integer("123"))     
print(is_integer("-456"))    
print(is_integer("12.3"))     