x:float = 5.0
y:float = 1.0 / x
print(x,y)
print(x*y)


x:float = -62.3
y:float = x%2.0

print(x)
print(y)



numero_uno:int = 34
numero_due:int = 23
numero_tre:int = 65
media:int =(numero_uno + numero_due + numero_tre)/3 
print(media)

print("2 \n0 \n2 \n5")


Fahrenheit = 74

Celsius = 5 * (Fahrenheit - 32) / 9

print(Celsius)



menu = {
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

ordine = {
    "Pasta": 10.50,
    "Cotoletta": 10.00,
    "Patatine Fritte": 5.50,
    "Acqua": 1.50,
    "Tiramisu": 6.00
}

totale = 0
totale += ordine["Pasta"]
totale += ordine["Cotoletta"]
totale += ordine["Patatine Fritte"]
totale += ordine["Acqua"]
totale += ordine["Tiramisu"]
print(totale, "Euro")


