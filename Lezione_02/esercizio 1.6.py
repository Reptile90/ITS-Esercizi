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


