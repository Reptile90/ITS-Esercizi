'''Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". 
Un numero magico è definito come un numero che contiene il numero 7.'''


def is_magic_number(num: int) -> bool:
    num = str(num)
    magic_number = "7"
    if magic_number in num:
        return True
    else:
        return False