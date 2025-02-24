'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

n1 = int(input("Digita un numero intero: "))
n2 = int(input("Digita un altro numero intero: "))

if n1 > n2:
  n1,n2 = n2,n1
prodotto=1
for i in range(n1,n2):

  prodotto *= i

print(f"il prodotto dei numeri compresi tra {n1} e {n2} è {prodotto}")