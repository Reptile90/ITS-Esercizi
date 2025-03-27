lista_acquisti = {}

def definizioneProdotto(nome:str, prezzo:float, quantità:int)->dict:
    return {"nome": nome, "prezzo": prezzo, "quantità": quantità}

def aggiungiProdotto(scelta_utente:str, prodotto:dict,quantità_da_rimuovere: int = 1):
    nome = prodotto["nome"]
    quantità = prodotto["quantità"]
    if scelta_utente == "compra":
        if nome in lista_acquisti:
            lista_acquisti[nome]["quantità"] += quantità
        else:
            lista_acquisti[nome] = prodotto
        print(f"{quantità}x {nome} aggiunto al carrello.")

    elif scelta_utente == "rimuovi":
        if nome in lista_acquisti:
                if lista_acquisti[nome]["quantità"] > quantità_da_rimuovere:
                    lista_acquisti[nome]["quantità"] -= quantità_da_rimuovere
                    print(f"{quantità_da_rimuovere}x {nome} rimosso dal carrello.")
                else:
                    lista_acquisti.pop(nome)
                print(f"{nome} eliminato dal carrello.")
        else:
            print(f"{nome} non è nel carrello.")
    else:
        print("Scelta non valida.")

def visualizzaCarrello():
    if not lista_acquisti:
        print("Il carrello è vuoto")
    else:
        print("\n il carrello attuale: ")
        for nome,dettagli in lista_acquisti.items():
            print(f"{dettagli['quantità']}x {nome} - {dettagli['prezzo']}€ ciascuno")
        print(f"Totale: {calcolaTotale()}€\n")

def calcolaTotale():
    totale = 0
    scelta_sconto = input("Vuoi inserire uno sconto? Digita 'Si o No': ").lower()
    if scelta_sconto == "si":
        sconto = int(input("inserisci sconto:"))
    for dettagli in lista_acquisti.values():
        
        totale += dettagli["prezzo"] * dettagli["quantità"]
        totale_sconto = totale - (totale * sconto / 100)
        totale_iva = totale_sconto + (totale_sconto * 22 / 100)
        

    return round(totale_iva, 2)


prodotto1 = definizioneProdotto("Mela", 0.50, 10)
prodotto2 = definizioneProdotto("Banana", 0.30, 5)
prodotto3 = definizioneProdotto("Arancia", 0.80, 8)

aggiungiProdotto("compra", prodotto1)
aggiungiProdotto("compra", prodotto2)
aggiungiProdotto("compra", prodotto3)

visualizzaCarrello()

aggiungiProdotto("rimuovi", prodotto2, 2)

visualizzaCarrello()