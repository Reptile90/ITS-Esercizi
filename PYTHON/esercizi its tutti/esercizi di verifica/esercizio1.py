'''Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.'''

def countdown(number:int)->int:
    while number >= 0:
        print(number)
        number-= 1

countdown()