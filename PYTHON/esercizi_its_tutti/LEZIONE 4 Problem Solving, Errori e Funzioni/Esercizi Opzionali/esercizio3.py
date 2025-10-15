'''Carrello della spesa E-commerce:

Crea una funzione che definisce un prodotto con un nome, un prezzo e una quantità. 
Crea una funzione che gestisce il carrello della spesa, consentendo all'utente di aggiungere, rimuovere e visualizzare i prodotti nel carrello. 
La funzione dovrebbe calcolare il totale del carrello e applicare eventuali sconti o tasse. 
Implementa un ciclo for per iterare sugli articoli nel carrello e stampare informazioni dettagliate su ciascun prodotto e sul totale.'''


def crea_prodotto(nome:str, prezzo:float, quantita:int)->dict:
    if not isinstance(nome, str) or nome == "": #controlllo che il nome sia effettivamente una stringa
        print("Errore: Il nome deve essere una stringa non vuota.")
        return None
    if not isinstance(prezzo, (int, float)) or prezzo < 0:  #controllo che il prezzo sia effettivamente un intero o un float
        print("Errore: Il prezzo deve essere un numero non negativo.")
        return None
    if not isinstance(quantita, int) or quantita <= 0: #controllo che la quantità sia un numero intero
        print("Errore: La quantità deve essere un intero positivo.")
        return None
    
    prodotto:dict = {  #creo un dizionario dove andro ad inserire come argomenti, il nome, prezzo e quantità
        "nome":nome,
        "prezzo": float(prezzo),
        "quantita":int(quantita)
    }
    return prodotto #ritorna il dizionario con le informazioni del prodotto


carrello = [] #inizializzo una variabile carrello vuora che sarà una lista di prodotti
print(f"Carrello inizializzato {carrello}")

def aggiungi_prodotto(carrello_dest:list, nome:str, prezzo:float, quantita:int):
    nuovo_prodotto = crea_prodotto(nome, prezzo, quantita) #creo una variabile nuova di un prodotto e inserisco la funzione precedentemente creata

    if nuovo_prodotto: #controllo ritornato True se i dati inseriti sono validi
        carrello_dest.append(nuovo_prodotto) #inserisco il prodotto nel carrello di destinazione
        print(f"'{nome}' aggiunto al carrello.")
    else:
        print(f"'{nome}' non aggiunto a causa di dati non validi.")


def rimuovi_prodotto(carrello_target:list, nome_prodotto_da_rimuovere:str)->bool:

    prodotto_trovato = False #creo una variabile con cui adro a verificare se il prodotto è presente o no
    indice_da_rimuovere = -1 #creo una variabile che mi consenta di stabili quanti prodotto deve rimuovere ad ogni chiamata della funzione

    for i in range (len(carrello_target)): #iterazione con un ciclo fro per ogni indice del carrello
        if carrello_target[i]['nome'].lower() == nome_prodotto_da_rimuovere.lower(): #verifico se l'indice della lista è uguale al prodotto da rimuovere richiesto dall'utente
            indice_da_rimuovere = i 
            prodotto_trovato = True
            break #se il prodotto è stato trovato usciamo dal ciclo
    
    if prodotto_trovato:
        prodotto_rimosso = carrello_target.pop(indice_da_rimuovere) #rimuoviamo l'elemento
        print(f"'{prodotto_rimosso['nome']}' rimosso dal carrello.")
        return True #ritorniamo true se il prodotto è stato rimosso correttamente
    else:
        print(f"Prodotto '{nome_prodotto_da_rimuovere}' non trovato nel carrello.")
        return False #ritorniamo false se il prodotto non è presente nel carrello


print(f"Carrello dopo rimozioni: {carrello}")

def visualizza_carrello(carrello_da_vedere):
    if not carrello_da_vedere: #Controlla se la lista è vuota.
        print("Il carrello è vuoto")
    else:
        for prodotto in carrello_da_vedere:
            print(f"- Prodotto: {prodotto['nome']}, Quantità: {prodotto['quantita']}, Prezzo Unitario: €{prodotto['prezzo']:.2f}")
        print("-----------------------------\n")



def calcola_totale_lordo(carrello_da_calcolare)->float:
    totale = 0.0 #creo una variabile vuota che rappresentera il totale calcolato
    for prodotto in carrello_da_calcolare: #itero per ogni prodotto 
        totale += prodotto['prezzo'] * prodotto['quantita']#il totale è uguale al prezzo del prodotto * la quantità
    return totale

SOGLIA_SCONTO = 50.0
PERCENTUALE_SCONTO = 0.10 #percentuale del 10% di sconto
ALIQUOTA_IVA = 0.22 #22%

def applica_sconti_tasse(totale_lordo)->tuple:
    sconto= 0.0 #imposto lo sconto a 0
    totale_scontato = totale_lordo #il totale scontato inizialmente è uguale al lordo
    if totale_lordo > SOGLIA_SCONTO: #verifico se il totale lordo è maggiore della soglia impostata
        
        sconto = totale_lordo * PERCENTUALE_SCONTO # lo sconto è il risultato dal totale * la percentuale sconto
        totale_scontato = totale_lordo - sconto #totale scontato è la sottrazione dal totale dello sconto
        print(f"Applicato sconto del {PERCENTUALE_SCONTO*100:.0f}%: -€{sconto:.2f}")
    else:
        print("Nessuno sconto applicato (soglia non raggiunta).")

    iva = totale_scontato * ALIQUOTA_IVA #definisco la variabile iva che è uguale al totale scontato + l'aliquota iva stabilita
    totale_netto = totale_scontato + iva #il netto è uguale al totale scontato + l'iva
    print(f"Aggiunta IVA ({ALIQUOTA_IVA*100:.0f}%): +€{iva:.2f}")

    return totale_netto, sconto, iva  #ritorna il netto, lo sconto effettuato e l'iva sul prodotto

# Passaggio 8: Funzione di riepilogo che itera e stampa tutto
def stampa_riepilogo_carrello(carrello_completo):

    print("\n========== RIEPILOGO CARRELLO ==========")
    if not carrello_completo: #verifica se il carrello è vuoto
        print("Il carrello è vuoto.")
        print("======================================")
        return # Esce dalla funzione se il carrello è vuoto

    # 1. Iterare sugli articoli e stampare informazioni dettagliate (ciclo for)
    print("Articoli nel carrello:")
    for prodotto in carrello_completo:
        costo_articolo = prodotto['prezzo'] * prodotto['quantita']
        print(f"  - {prodotto['nome']} ({prodotto['quantita']} x €{prodotto['prezzo']:.2f}) = €{costo_articolo:.2f}")

    print("--------------------------------------")

    # 2. Calcolare il totale lordo
    totale_lordo = calcola_totale_lordo(carrello_completo)
    print(f"Subtotale (Lordo): €{totale_lordo:.2f}")

    # 3. Applicare sconti e tasse
    # Riutilizziamo la funzione precedente, ma stampiamo i messaggi qui per coerenza
    sconto_calc = 0.0
    totale_per_iva = totale_lordo
    if totale_lordo > SOGLIA_SCONTO:
        sconto_calc = totale_lordo * PERCENTUALE_SCONTO
        totale_per_iva = totale_lordo - sconto_calc
        print(f"Sconto ({PERCENTUALE_SCONTO*100:.0f}% su €{totale_lordo:.2f}): -€{sconto_calc:.2f}")
    else:
        print("Sconto: €0.00 (soglia non raggiunta)")

    iva_calc = totale_per_iva * ALIQUOTA_IVA
    totale_netto = totale_per_iva + iva_calc
    print(f"IVA ({ALIQUOTA_IVA*100:.0f}% su €{totale_per_iva:.2f}): +€{iva_calc:.2f}")
    print("--------------------------------------")

    # 4. Stampare il totale finale
    print(f"TOTALE FINALE: €{totale_netto:.2f}")
    print("======================================")




print("\n--- Aggiunta prodotti ---")
aggiungi_prodotto(carrello, "Maglietta", 15.99, 2)
aggiungi_prodotto(carrello, "Pantaloni", 29.99, 1)
aggiungi_prodotto(carrello, "Scarpe", 59.90, 1)
aggiungi_prodotto(carrello, "Cappello", 10.00, 3)
aggiungi_prodotto(carrello, "Zaino", 45.50, 1)
aggiungi_prodotto(carrello, "Orologio", 120.00, 1)
aggiungi_prodotto(carrello, "Occhiali", 75.00, 2)
aggiungi_prodotto(carrello, "Cintura", 20.00, 1)
aggiungi_prodotto(carrello, "Guanti", 18.00, 2)
aggiungi_prodotto(carrello, "Sciarpa", 12.50, 1)

# Aggiunta di prodotti con errori
aggiungi_prodotto(carrello, "", 25.00, 1)           # Nome vuoto
aggiungi_prodotto(carrello, "Anello", -5.00, 1)      # Prezzo negativo
aggiungi_prodotto(carrello, "Bracciale", 15.00, 0)   # Quantità zero
aggiungi_prodotto(carrello, "Collana", "venti", 1)   # Prezzo non numerico
aggiungi_prodotto(carrello, "Portafoglio", 30.00, -2) # Quantità negativa

# Altri prodotti validi
aggiungi_prodotto(carrello, "Portachiavi", 5.00, 4)
aggiungi_prodotto(carrello, "Calze", 8.00, 5)
aggiungi_prodotto(carrello, "Felpa", 35.00, 1)
aggiungi_prodotto(carrello, "Giacca", 89.99, 1)
aggiungi_prodotto(carrello, "Laptop", 999.99, 1)

# Visualizzazione del carrello attuale
print("\n--- Visualizzazione carrello ---")
visualizza_carrello(carrello)

# Rimozione prodotti
print("\n--- Rimozione prodotti ---")
rimuovi_prodotto(carrello, "Cappello")      # Prodotto esistente
rimuovi_prodotto(carrello, "Laptop")        # Prodotto esistente
rimuovi_prodotto(carrello, "Tablet")        # Prodotto non esistente

# Visualizzazione carrello dopo rimozioni
print("\n--- Carrello aggiornato ---")
visualizza_carrello(carrello)

# Riepilogo finale
print("\n--- Riepilogo Finale ---")
stampa_riepilogo_carrello(carrello)

