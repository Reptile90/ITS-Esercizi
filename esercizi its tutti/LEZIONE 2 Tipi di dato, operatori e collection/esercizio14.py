'''3-10. Every Function: Think of things you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''


things:list[str] = ["Appennino", "Po", "Tevere", "California", "Los Angeles", "Italiano", "Python"]


things.append("Java")
print(things)

things.pop(0)
print(things)

things.insert(3,"Kubernetes")
print(things)

things.sort()
print(things)

things.reverse()
print(things)

things.pop(1)
print(things)

things.sort(reverse=True)
print(things)

things.clear()
print(things)