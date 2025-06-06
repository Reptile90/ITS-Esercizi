'''Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10,
d) 5, 15, 25, 35, 45
'''
#ciclo while a) 2, 4, 6, 8, 10, 12, 14
cont = 2

while cont <= 14:
    print(cont)
    cont+= 2
print("-"* 30)

#ciclo for a) 2, 4, 6, 8, 10, 12, 14
for n in range(2,15,2):
    print(n)
print("-"* 30)

#ciclo while b) 1, 4, 7, 10, 13
cont1 = 1

while cont1 <= 13:
    print(cont1)
    cont1 += 3
print("-"* 30)

#ciclo for b) 1, 4, 7, 10, 13
for num in range(1,14,3):
    print (num)
print("-"* 30)


#ciclo while c) 30, 25, 20, 15, 10,
cont2 = 30

while cont2 >= 0:
    print (cont2)
    cont2 -= 5

print("-"* 30)
#ciclo for c) 30, 25, 20, 15, 10,
for num1 in range(30,-1,-5):
    print(num1)
print("-"* 30)

#ciclo while d) 5, 15, 25, 35, 45
cont3 = 5

while cont3 <= 45:
    print(cont3)
    cont3 += 10
print("-"* 30)

#ciclo for d) 5, 15, 25, 35, 45
for num2 in range(5,46,10):
    print(num2)

print("-"* 30)





