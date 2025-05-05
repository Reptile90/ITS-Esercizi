def seconds_since_noon(ore,minuti,secondi)->int:
    secondi_ore = ore * 3600
    secondi_minuti = minuti *60

    totale_secondi = secondi_ore + secondi_minuti + secondi

    return totale_secondi


def time_difference(ore1,minuti1,secondi1,ore2,minuti2,secondi2)->int:
    difference = abs(seconds_since_noon(ore1,minuti1,secondi1) - seconds_since_noon(ore2,minuti2,secondi2))

    return difference





print(time_difference(0, 0, 0, 12, 0, 0))
print(time_difference(1, 0, 0, 3, 15, 30))