'''Sistema di Valutazione Scolastica
Crea una funzione che prenda in input il nome di uno studente e i suoi voti in diverse materie.
La funzione calcola la media dei voti e stampa il nome dello studente, la media e un messaggio che indica se lo studente ha superato l'esame (media ≥ 60) oppure non lo ha superato.

Crea un ciclo for per iterare su una lista di studenti e relativi voti, chiamando la funzione per ogni studente.'''


def calcola_valutazione(nome: str, voti: list[int]) -> float:
    if not voti:
        print(f"{nome} non ha voti registrati.")
        return 0.0

    media = sum(voti) / len(voti)

    if media >= 60:
        print(f"{nome} ha superato l'esame con una media di {media:.2f}")
    else:
        print(f"{nome} non ha superato l'esame. Media: {media:.2f}")

    return media


studenti = [
    ("Mario Rossi", [70, 65, 80]),
    ("Luca Bianchi", [50, 55, 45]),
    ("Anna Verdi", [90, 85, 88]),
    ("Giulia Neri", []),
]
for nome, voti in studenti:
    calcola_valutazione(nome, voti)
