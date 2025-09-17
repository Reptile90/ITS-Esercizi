import random

def indovina_numero():
    numero_casuale = random.randint(1, 5)
    max_tentativi = 3
    cont = 0

    while cont < max_tentativi:
        scelta = int(input("Indovina il numero (tra 1 e 5): "))

        if scelta < numero_casuale:
            print("Numero scelto troppo basso.")
            cont += 1
        elif scelta > numero_casuale:
            print("Numero scelto troppo alto.")
            cont += 1
        else:
            print(f"Il numero {scelta} è il numero giusto!")
            break

        if cont == max_tentativi:
            print(f"I tentativi sono esauriti! Il numero era {numero_casuale}.")

indovina_numero()
