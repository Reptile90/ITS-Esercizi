def binary_search(lista, numero):
    start = 0 #imposto l'indice 0
    end = len(lista) - 1 #imposto l'indice finale
    mid =  end // 2 

    while lista[start] <= lista[end]: #fino a che start non sarà uguale a end
    
        if lista[mid] == numero: #se l'indice mid è uguale al target ritorna true
            return True
        elif lista[mid] < numero: #altrimenti cerca sia a destra che a sinistra se presente il numero
            start = mid + 1
        else:
            end = mid - 1

        return False


numeri = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(numeri, 7))
print(binary_search(numeri, 4))