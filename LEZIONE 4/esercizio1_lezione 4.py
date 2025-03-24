'''Crea una funzione che prenda il nome di uno studente e i suoi punteggi in diverse materie come input.
La funzione calcola il punteggio medio e stampa il nome dello studente, la media e un messaggio che indica se lo studente ha superato l'esame (media >= 60) o ha fallito.
Crea un ciclo for per iterare su un elenco di studenti e punteggi, chiamando la funzione per ogni studente.'''


def calcolaVoto(nome:str, punteggio:list[int]):
    media = sum(punteggio) / len(punteggio)
    if media >= 60:
        print(f"{nome} hai superato l'esame con {media:.2f}")
    else:
        print(f"{nome} Hai totalizzato {media:.2f} punti. Esame fallito")
studenti={}
while True:
    nome = input("Digita il tuo nome: ").lower()
    if nome == "fine":
        break
    punteggio:list[int] = []
    while True:
        punti= int(input("Digita il punteggio ottenuto o digita 0 per confermare il risultato: "))
        if punti == 0:
            break
        punteggio.append(punti)
    studenti[nome]= punteggio

for nome, punteggio in studenti.items():
    calcolaVoto(nome, punteggio)