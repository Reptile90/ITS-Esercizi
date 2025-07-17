from datetime import datetime, timedelta

if __name__ == "__main__":

    
    u1 = UtentePrivato("abcd")
   

    # username duplicato
    try:
        u1_dup = UtentePrivato("abcd")
    except ValueError as e:
        print("Errore atteso (username duplicato):", e)

    # creazione secondo utente
    u2 = UtentePrivato("cdef")
    print("Creato:", u2)

    # creazione di un bid valido
    b1 = Bid(u1)
    print("Creato:", b1)

    # creazione di un'asta valida
    now = datetime.now()
    a1 = Asta(prezzo=RealGZ(100),prezzo_bid=RealGZ(10),pubblicazione=now,scadenza=now + timedelta(minutes=10))
    

    # asta con prezzo negativo
    try:
        Asta(RealGZ(-1), RealGZ(5), now, now + timedelta(minutes=1))
    except ValueError as e:
        print("Errore atteso (prezzo negativo):", e)

    # asta con scadenza precedente alla pubblicazione
    try:
        Asta(RealGZ(1), RealGZ(1), now, now - timedelta(minutes=1))
    except ValueError as e:
        print("Errore atteso (scadenza < pubblicazione):", e)

    # associazione Bid_Ut
    Bid_Ut.add(u1, b1)
    

    # aggiunta bid a asta
    a1.aggiungi_bid(b1)
    print("Bid aggiunto all'asta")

    # bid duplicato in asta
    try:
        a1.aggiungi_bid(b1)
    except ValueError as e:
        print("Errore atteso (bid duplicato):", e)

    # link asta-bid
    Asta_Bid.add(a1, b1)
    print("Asta_Bid collegato")

    # cambiare prezzo dopo ricezione bid
    try:
        a1.set_prezzo(RealGZ(150))
    except ValueError as e:
        print("Errore atteso (modifica prezzo dopo bid):", e)

    # modifica scadenza dopo ricezione bid
    try:
        a1.set_scadenza(datetime.now() + timedelta(hours=1))
    except ValueError as e:
        print("Errore atteso (modifica scadenza dopo bid):", e)

    # calcolo prezzo attuale in tempo reale
    prezzo_attuale = a1.prezzo_attuale(datetime.now())
    print("Prezzo attuale:", prezzo_attuale)

    #vincitore
    vincitore = a1.vincitore()
    print("Vincitore:", vincitore)

    # bid con data dopo la scadenza
    try:
        b2 = Bid(u2)
        b2._Bid__istanteBid = datetime.now() + timedelta(hours=1)
        a1.aggiungi_bid(b2)
    except ValueError as e:
        print("Errore atteso (bid dopo scadenza):", e)

    # cancellazione utente
    u1.cancella_registrazione()

    # cancellazione utente già rimosso
    try:
        u1.cancella_registrazione()
    except KeyError as e:
        print("Errore atteso (utente già rimosso):", e)


