from string import ascii_lowercase

def caesar_cypher_encrypt(s:str, key:int)->str:
    encrypted_string = ""
    alphabet:str= ascii_lowercase
    
    
    

    for char in s:
        if char.isalpha():
            upp:bool = True if char.isupper() else False
            
            for index,letter in enumerate(s):
                if char.lower() == letter:
                    position = (index + key)% len(alphabet)
            if upp == True:
                encrypted_string += alphabet[position].upper()
            else:
                encrypted_string += alphabet[position]
        else:
            encrypted_string += char
    
    return encrypted_string





print(caesar_cypher_encrypt("stefano",40))




def caesar_cypher_decrypt(s:str,key:int)->str:
    pass