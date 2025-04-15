import re

def isInteger(numero:str):
    if int(re.match(r"-?\d+", numero).group()):
        return True
    elif float(re.match(r"-?\d+", numero).group()):
        return False
    else:
        return False
    




print(isInteger("123"))      # True
print(isInteger("-456"))     # True
print(isInteger("12.3"))     # False