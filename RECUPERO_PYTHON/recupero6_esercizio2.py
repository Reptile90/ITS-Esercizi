'''
Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe). L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza, oppure sono stati inseriti 30 nomi distinti. Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.
'''


cont = 0
lista_nomi=[]

while cont < 20:
    nome = input("Inserisci un nome: ").lower()
    if len(nome) > 20:
        print("Il nome deve avere al massimo 20 caratteri")
    else:

        if nome in lista_nomi or nome == "":
            break
        else:
            cont +=1
            lista_nomi.append(nome)
    

max=""

for n in lista_nomi:
    if len(n) > len(max):
        max = n



print(f"Hai inserito {cont} indistinti")
print(f"Il più lungo è {max.capitalize()} con {len(max)} caratteri")



