

def voto_esame(matricola,voto):

    if voto > 17:
        print("ESAME SUPERATO!!!!!!")
        print(f"Sei {matricola} e hai preso {voto}")
    elif voto == 17:
        print("Vai a fare l'orale!")
        voto_orale = input("Inserisci il voto dell'orale: ")
        if voto_orale > 17:
            print("ESAME SUPERATO!!!!!!")
            print(f"Sei {matricola} e hai preso {voto}")
        else:
            print("Sei stato BOCCIATO!!!!")
            print("Studia di più e rifai l'orale")
    else:
        print("Sei stato BOCCIATO!!!!")
        print("Studia di più")
        
matricola = input("Inserisci la tua matricola: ")
voto = int(input("Inserisci il tuo voto: "))       
voto_esame(matricola,voto)
    
    
    