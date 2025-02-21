'''Every Function: Think of things you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''

lista = ["inglese", "Italiano", "Tedesco", "Spagnolo", "Francese"]

lista.append("Giapponese")
print(lista)

lista.insert(3, "Greco")
print(lista)

lista.remove("Greco")
print(lista)

lista.insert(4, "Albanese")

lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.append("Rumeno")

lista2 = lista.copy()
print(lista2)

lista2.reverse()
print(lista2)

lista.extend(lista2)

lista.sort()
print(lista)

print(len(lista))


