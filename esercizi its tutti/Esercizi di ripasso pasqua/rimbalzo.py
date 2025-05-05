def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi < 5:

        if altezza >= 0:
            print(f'Tempo: {tempo} Altezza: {altezza}')
            altezza = altezza + velocita
            velocita = velocita - 96

        else:
            print(f'Tempo: {tempo} Rimbalzo!')
            rimbalzi += 1
            altezza = altezza * -0.5
            velocita = velocita * -0.5
        tempo += 1

rimbalzo()