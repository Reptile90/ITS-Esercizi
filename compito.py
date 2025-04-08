'''Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

For example:
Test 	Result

print(somma_elementi([1,1,1],[1,1,1]))

	

[2, 2, 2]'''

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(len(x)):
        somma = x[i] + y[i]
        result.append(somma)
        
    return result

# Esempio di utilizzo
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

print(somma_elementi(lista1, lista2))  # Output: [6, 8, 10, 12]


        





         


   
   
         
         
  



         
         
   
         

        
   
      
      
      





