'''Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. 
Il risultato deve essere visualizzato in output.'''

frase:str = input("Digita una frase a piacere: ")

cont:int = 0

for spazi in frase:
    if spazi == " ":
        cont+=1
print(f"Gli spazi contenuti nella frase digitata sono: {cont}")