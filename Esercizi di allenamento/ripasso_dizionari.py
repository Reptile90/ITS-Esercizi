studente:dict = {
    "Nome": "Stefano",
    "Età":"34",
    "Corso":"Application Cloud Developer"
}

studente["Email"]="stefano@mail.com"

print(studente)

for key in studente.keys():
    print(key)
    
for key,value in studente.items():
    print(key,":",value)
    
    
print(len(studente))

studente["Corso"]="Informatica"
print(studente)

studente.update({"Telefono":3333332})

print(studente)

del(studente["Email"])

print(studente)

print(studente.get("Corso"))

print(studente.get("Email"))


studente1={}

studente1.update({"Nome":"Lorenzo"})

studente1["Corso"]="Application Cloud Developer"
print(studente1)

nuovo= studente.pop("Telefono")

print(nuovo)


nomi =["Anna","Luca","Francesco"]

eta = [22,25,27]

dictionary={}

for nome,eta1 in zip(nomi,eta):
    dictionary[nome]= eta1

    
print(dictionary)


nuovodiz= {x:x**2 for x in range(5)}

print(nuovodiz)


voti= {"matematica":6, "italiano":7, "Informatica":10, "Inglese":9, "Geometria":4, "storia":None}

sum= 0
media=0
for value in voti.values():
    if value == None:
        continue
    sum+=value
    
media = sum/len(voti)
print(media)


max = 0

for value in voti.values():
    if value == None:
        continue
    if value > max:
        max = value
        
print(max)

da_rimuovere = [key for key,value in voti.items() if value is None]
for key in da_rimuovere:
    del voti[key]
        
        
print(voti)