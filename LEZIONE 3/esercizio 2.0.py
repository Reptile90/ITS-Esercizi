frase:str = input("Inserisci una frase: ")
frase:str = frase.title()

parole:list[str] = frase.split()

result: list[str] = []

for parola in parole:
	p_in = parola[:-1]
	p_ultima = parola[-1]
	nuova = p_in + p_ultima.upper()
	result.append(nuova)
	
print(" ".join(result))





