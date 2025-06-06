'''Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.'''

def verify_xyz(x:bool, y:bool, z:bool):

    if x and (y or z):
        return "Azione permessa"
    
    else:
        return "Azione negata"
    


print(verify_xyz(True, False, False))

print(verify_xyz(True, True, False))

print(verify_xyz(False, True, True))