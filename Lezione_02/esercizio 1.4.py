'''Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

2
0
2
4'''

print("2 \n0 \n2 \n5")


n = int(input("inserisci un numero a 4 cifre"))
m = n // 1000
c = n // 100 - m * 10
d = n // 10 - m *100 - c*10
u = n - m * 1000 - c*100 - d*10

print(m)
print(c)
print(d)
print(u)
