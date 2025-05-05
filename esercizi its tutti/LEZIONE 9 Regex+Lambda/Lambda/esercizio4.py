'''Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]. Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.
'''



studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]


sorted_by_age = sorted(studenti, key= lambda age: age[1])

print(sorted_by_age)