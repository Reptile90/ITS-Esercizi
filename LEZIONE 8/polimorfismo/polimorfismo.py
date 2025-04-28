from alieno import Alieno
from persona import Persona


#creare un oggetto p della classe persona

p:Persona = Persona("Stefano","Reali",34)

#visualizziamo le informazioni della Persona P
print(p)

#creare un oggetto et della classe Alieno
et:Alieno = Alieno("Andromeda")

#visualizziamo le informazioni dell'Alieno ET
print(et)

#l'oggetto p invoca il metodo speak()
p.speak()

#l'oggetto et invoca il metodo speak()
et.speak()