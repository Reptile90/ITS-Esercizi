'''Text Analysis:

Create a function that takes a paragraph and counts the number of occurrences of each word.
The function should print a report showing the most frequent words and their number of occurrences.
You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
Implement error handling to handle missing files or other input issues.
'''
import string
import os

def leggi_testo_da_file(percorso_file)->str:

    if not os.path.exists(percorso_file): #controlla se è esistente il file
        print(f"Errore: Il file '{percorso_file}' non è stato trovato.")
        return None
    try:
        with open(percorso_file, 'r', encoding='utf-8') as file: #apro il file
            testo = file.read()
        return testo
    except FileNotFoundError: # Anche se abbiamo controllato, è buona norma tenerlo
        print(f"Errore: Il file '{percorso_file}' non è stato trovato.")
        return None
    except Exception as e: # Gestisce altri possibili errori di lettura
        print(f"Errore durante la lettura del file '{percorso_file}': {e}")
    return None


def analizza_paragrafo(testo_input, top_n=10):

    if not testo_input or not isinstance(testo_input,str):#controlla se il file non è vuota e se siano stringhe
        print("Errore: Input non valido. Fornire una stringa di testo non vuota.")
        return #esce dalla funzione se non è valido
    
    testo_minuscolo = testo_input.lower()
    tabella_rimozione_punteggiatura = str.maketrans('', '', string.punctuation)
    testo_pulito = testo_minuscolo.translate(tabella_rimozione_punteggiatura)

    parole = testo_pulito.split()

    # Controllo se ci sono parole dopo la pulizia
    if not parole:
        print("Errore: Il testo non contiene parole valide dopo la pulizia.")
        print("--- Fine Analisi ---")
        return
    print(f"Numero totale di parole (dopo pulizia): {len(parole)}")

    conteggio_parole = {}
    for parola in parole:
        conteggio_parole[parola] = conteggio_parole.get(parola, 0) + 1
    
    parole_ordinate = sorted(conteggio_parole.items(), key=lambda item: item[1], reverse=True)
    print(f"\n--- Report Frequenza Parole (Top {top_n}) ---")
    num_parole_da_stampare = min(top_n, len(parole_ordinate))
    if num_parole_da_stampare == 0:
        print("Nessuna parola da mostrare nel report.")
    else:
        for i in range(num_parole_da_stampare):
            parola, conteggio = parole_ordinate[i]
            print(f"{i+1}. '{parola}': {conteggio} occorrenze")

    print("----------------------------------------")
    print("--- Fine Analisi ---")



# Passaggio 5: Esempio di utilizzo
if __name__ == "__main__":
    # Esempio 1: Analisi di una stringa di testo diretta
    paragrafo_esempio = """
    Questo è un testo di esempio. Serve per testare la funzione di analisi del testo.
    L'analisi conta le parole, e questo testo contiene parole ripetute.
    Esempio di parole: testo, parole, analisi. Contare bene è importante!
    """
    analizza_paragrafo(paragrafo_esempio, top_n=5) # Mostra le top 5 parole

    print("\n******************************************\n")

    # Esempio 2: Analisi da file
    # Creiamo un file di esempio temporaneo
    nome_file_esempio = "testo_esempio.txt"
    contenuto_file = """
    Riga uno del file di testo.
    Seconda riga con altre parole, parole e ancora parole.
    Il file serve come input per testare la lettura da file e l'analisi.
    Testare, testare, testare! Punteggiatura? Sì!
    """
    try:
        with open(nome_file_esempio, 'w', encoding='utf-8') as f:
            f.write(contenuto_file)
        print(f"File '{nome_file_esempio}' creato per il test.")

    # Leggiamo il testo dal file usando la nostra funzione ausiliaria
        testo_da_file = leggi_testo_da_file(nome_file_esempio)

    # Se la lettura ha avuto successo, analizziamo il testo
        if testo_da_file:
            analizza_paragrafo(testo_da_file, top_n=7) # Mostra le top 7

    except Exception as e:
        print(f"Errore nella creazione/gestione del file di test: {e}")
    finally:
        # Pulizia: rimuoviamo il file di esempio se esiste
        if os.path.exists(nome_file_esempio):
            os.remove(nome_file_esempio)
            print(f"File '{nome_file_esempio}' rimosso.")

    print("\n******************************************\n")

    # Esempio 3: Test dell'errore file non trovato
    print("Test lettura file non esistente:")
    testo_inesistente = leggi_testo_da_file("file_che_non_esiste.txt")
    if testo_inesistente is None:
        # Se leggi_testo_da_file restituisce None, l'errore è già stato stampato
        # Possiamo decidere se chiamare analizza_paragrafo con None (che stamperà un errore)
        # o semplicemente non chiamarlo.
        analizza_paragrafo(testo_inesistente) # Questo mostrerà l'errore di input non valido