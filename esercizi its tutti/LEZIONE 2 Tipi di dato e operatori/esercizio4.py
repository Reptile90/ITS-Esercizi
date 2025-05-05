'''Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

2
0
2
4'''




anno:int = 1990

migliaia = anno / 1000
n = anno % 1000
print (int(migliaia))
centinaia = n/100
n= n % 100
print(int(centinaia))
decine = n/10
n = n % 10
print(int(decine))
unita = n/1
n = n % 1
print(int(unita))