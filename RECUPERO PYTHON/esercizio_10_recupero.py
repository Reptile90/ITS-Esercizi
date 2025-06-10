def binary_search(lista, target):
    start = 0 #imposto l'indice 0
    end = len(lista) - 1 #imposto l'indice finale

    while start <= end: #fino a che start non sia uguale a end
        mid = (start + end) // 2 #l'indice mid è uguale a start + end /2 restituendo un intero
        if lista[mid] == target: #se l'indice mid è uguale al target ritorna true
            return True
        elif lista[mid] < target: #altrimenti cerca sia a destra che a sinistra se presente il numero
            start = mid + 1
        else:
            end = mid - 1

    return False


numeri = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numeri, 7))
print(binary_search(numeri, 4))