from string import ascii_lowercase

def caesar_cypher_encrypt(s,key):
    encrypted:str = ""

    for index, letter in enumerate(s):
        if letter.isalpha(): #verifico se letter non è un simbolo speciale o uno spazio
            if letter.islower(): #verifico se letter è minuscola
                alphabet = ascii_lowercase #creo la variabile alphabet in lowercase

            index = alphabet.index(letter) #indice della lettera nell'alfabeto
            new_position = (index+key) % len(alphabet) #la posizione corretta deve essere il il modulo di indice+key
            encrypted += alphabet[new_position] # aggiungo la lettera nella nuova posizione
        else:
            encrypted += letter #se non si verifica nulla, ritorna normale

    return encrypted


def caesar_cypher_decrypt(s,key):
    decrypted:str = ""

    for index, letter in enumerate(s):
        if letter.isalpha(): #verifico se letter non è un simbolo speciale o uno spazio
            if letter.islower(): #creo la variabile alphabet in lowercase
                alphabet = ascii_lowercase #creo la variabile alphabet in lowercase

            index = alphabet.index(letter) #indice della lettera nell'alfabeto
            new_position = (index-key) % len(alphabet) #la posizione corretta deve essere il il modulo di indice-key
            decrypted += alphabet[new_position] # aggiungo la lettera nella nuova posizione
        else:
            decrypted += letter #se non si verifica nulla, ritorna normale

    return decrypted



print(caesar_cypher_encrypt("stefano", 200))

print(caesar_cypher_decrypt("klwxsfg",200))