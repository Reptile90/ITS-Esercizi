'''Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119
E così via per tutta la stringa.
Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor'''

def crittografia(stringa:str,key:int):
    
    crittografato:list = []
    
    for char in stringa:
        charAscii = ord(char)
        encrypted = charAscii ^ key
        crittografato.append(encrypted)
    return crittografato


def decriptazione(cript:list, key:int):
    decrypt= ""
    for n in cript:
        newascii = n ^ key
        decrypt += chr(newascii)
        
    return decrypt
        
        
        
               
  
   
   
   
   
   
   
stringa = input("Inserisci la stringa da convertire: ")
key= int(input("Inserisci la chiave: "))
print(crittografia(stringa,key))


crittograta = crittografia(stringa, key)

print(decriptazione(crittograta,key))