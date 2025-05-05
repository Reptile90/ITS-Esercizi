'''Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.'''

def check_parentheses(expression: str) -> bool:
    cont = 0
    for carattere in expression:
        if carattere == "(":
            cont += 1
        elif carattere == ")":
            cont -= 1
        
        if cont < 0:
            return False
    return cont == 0