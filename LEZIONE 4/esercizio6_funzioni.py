'''Password Generator:

Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
Allow the user to specify the password length and desired character types.
Generate and return a random password that meets the user's criteria.'''

import random
import string

def passwordGenerator(lunghezza:int, minuscola:bool=True, maiuscola:bool=True, numeri:bool =True, simboli:bool= True)->str:
    caratteri:str = ""

    if minuscola:
        caratteri += string.ascii_lowercase
    if maiuscola:
        caratteri += string.ascii_uppercase
    if numeri:
        caratteri += string.digits
    if simboli:
        caratteri += string.punctuation

    if not caratteri:
        print("Seleziona un almeno un tipo carattere per generare la password")

    password = ""

    for _ in range(lunghezza):
        password += random.choice(caratteri)
    return password
    

print(passwordGenerator(12, True, True, True, True))
print(passwordGenerator(8, True, False, True, False))