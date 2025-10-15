import re

def is_integer(s)->bool:
    return bool(re.fullmatch(r"-?\d+", s))     # ^. Garantisce che il match parta dall'inizio.
                                                #-? Segno meno opzionale. Il simbolo ? indica che - può esserci o no.
                                                #\d Una o più cifre. \d corrisponde a qualsiasi cifra da 0 a 9; + richiede almeno una







print(is_integer("123"))     # True
print(is_integer("-456"))    # True
print(is_integer("12.3"))     # False