'''#dal file persona.py importa la classe Persona
from persona import Persona

#creo una persona
sr:Persona = Persona("Stefano", "Reali", 34)

print(sr)

print(sr.name, sr.last_name,sr.age)

#richiamare la funzione displayData per mostrare in output i dati relativi alla persona sr

sr.displayData()

print("-----------")'''

#dal file persona2 importa la classe Persona

from persona2 import Persona

sr:Persona = Persona()

#richiamo la funziona displayData per mostrare le informazioni relative all'oggetto sr

#sr.displayData()


#modificare il nome della persona sr

sr.setName("Stefano")

#modificare il cognome della persona sr
sr.setLastname("Reali")
#modificare l'età della persona sr
sr.setAge(34)

sr.displayData()

print(sr.getName(),sr.getLastname(),sr.getAge())