
def transform(x: int) -> int:
    if x % 2 == 0:
        x = x / 2
    else:
        x = (x * 3)-1
    return x


print(transform(4))

print(transform(-10))



def calcola_stipendio(ore_lavorate: int) -> float:
    stipendio_orario = 10
    cont_strao = 0
    cont_ore = 0
    straordinario = stipendio_orario * 1.5
    if ore_lavorate  > 40:
        cont_ore = 40
        cont_strao = ore_lavorate - 40
        stipendio_totale = (stipendio_orario * cont_ore) + (stipendio_orario * 1.5 * cont_strao)
    else:
        stipendio_totale = stipendio_orario * ore_lavorate

    return stipendio_totale


print(calcola_stipendio(40))
print(calcola_stipendio(0))
print(calcola_stipendio(45))
print(calcola_stipendio(60))



def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1,8):
        print(i)

    print("Sequenza b):")
    x = 3
    y = 5
    for i in range(5):

        print(x + i * y )

    print("Sequenza c):")
    x=20
    for i in range(6):
        print(x-6*i)

    print("Sequenza d):")
    x = 19
    for i in range(5):
        print(x+8*i)
    
    return



print_seq()
        
    
