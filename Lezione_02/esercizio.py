#esercizio 1
x:float = 5.0
y:float = 1.0 / x
print(x,y)
print(x*y)
print(x-y)

#esercizio 2

x:float = -62.3
y:float = x%2.0

print(x)
print(y)

#esercizio 3

numero_uno:int = 34
numero_due:int = 23
numero_tre:int = 65
media:int =(numero_uno + numero_due + numero_tre)/3 
print(f"La media è {media}")
#esercizio 4


print("2 \n0 \n2 \n5")

#esercizio 5

Fahrenheit = 74

Celsius = 5 * (Fahrenheit - 32) / 9

print(f"La temperatura è di {Celsius} gradi Celsius")

#esercizio 6

menu:dict = {
    "Pizza" : 9.00, 
    "Pasta" : 10.50,
    "Zuppa" : 7.00,
    "Hamburger": 15.50,
    "Cotoletta" : 10.00,
    "Salmone": 20.20,
    "Patatine Fritte": 5.50,
    "Verdura del giorno": 7.00,
    "Cheesecake": 6.00,
    "Tiramisu": 6.00,
    "Focaccia con nutella" : 6.00,
    "Coca Cola": 3.50,
    "Acqua": 1.50,
    "Vino": 5.00
    
}

ordine:dict ={} 
ordine["Pasta"]=9.00 
ordine["Cotoletta"] = 10.00
ordine["Patatine Fritte"] = 5.50
ordine["Acqua"] = 1.50
ordine["Tiramisu"] = 6.00


totale = 0
totale += ordine["Pasta"]
totale += ordine["Cotoletta"]
totale += ordine["Patatine Fritte"]
totale += ordine["Acqua"]
totale += ordine["Tiramisu"]
print(f"il totale è di {totale} Euro")


