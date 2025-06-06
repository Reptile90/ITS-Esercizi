'''Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali'''

def order_price(products:dict[str,float])->dict:

    new_products:dict[str,float]= {}
    prod_ten:float = 0.00

    for product, price in products.items():
        if price < 50:
            prod_ten = price + (price * 0.1)
            new_products[product] = round(prod_ten, 2)
        else:
            #new_products[product] = price
            continue

    return new_products








lista_prodotti:dict[str,float] = {"Cacciavite": 2.59, "Lampadina": 3.99, "Trapano": 59.99,"Rubinetto": 49.990}
print(order_price(lista_prodotti))