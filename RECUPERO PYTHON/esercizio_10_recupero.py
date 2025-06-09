def binary_search(lista, target):
    inizio = 0 #imposto l'indice 0
    fine = len(lista) - 1 #imposto l'indice finale

    while inizio <= fine: #fino a che inizio non sia uguale a fine
        medio = (inizio + fine) // 2 #l'indice medio è uguale a inizio + fine /2 restituendo un intero
        if lista[medio] == target: #se l'indice medio è uguale al target ritorna true
            return True
        elif lista[medio] < target: #altrimenti cerca sia a destra che a sinistra se presente il numero
            inizio = medio + 1
        else:
            fine = medio - 1

    return False


numeri = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numeri, 7))
print(binary_search(numeri, 4))