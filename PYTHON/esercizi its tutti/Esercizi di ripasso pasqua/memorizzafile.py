def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi: int = 1000
    dimensione_blocco: int = 512
    blocchi_disponibili: int = spazio_totale_blocchi

    for dimensione in files:
        compresso: float = float(dimensione * 80) / 100

        if compresso == 0:
            blocchi_necessari: int = 0
        else:
            blocchi_necessari_float = compresso / dimensione_blocco
            blocchi_necessari: int = round(blocchi_necessari_float)
            if blocchi_necessari == 0 and compresso > 0:
                blocchi_necessari = 1
        if blocchi_necessari <= blocchi_disponibili:
            blocchi_disponibili -= blocchi_necessari
            print(f"File di {dimensione} byte compresso in {compresso} byte e memorizzato. Blocchi usati: {blocchi_necessari}. Blocchi rimanenti: {blocchi_disponibili}.")
        else:
            print(f"Non è possibile memorizzare il file di {dimensione} byte. Spazio insufficiente.")
            break


memorizza_file([1100, 20000, 1048576, 512, 5000])