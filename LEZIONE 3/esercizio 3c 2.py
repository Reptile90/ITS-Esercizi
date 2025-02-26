'''Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0

- - - - - - - - - - - - - - - - -

Inserisci il voto di laurea: 65
Output: Voto non valido'''


voto_laurea:int = int(input("Inserisci un voto compreso da 66 a 110: "))
    
    

match voto_laurea:
    case voto_laurea if voto_laurea >= 106 and voto_laurea <= 110:
            print("GPA 4.0")
    case voto_laurea if voto_laurea >= 101 and voto_laurea <= 105:
            print("GPA 3.7")
    case voto_laurea if voto_laurea >= 96 and voto_laurea <= 100:
            print("GPA 3.3")
    case voto_laurea if voto_laurea >= 91 and voto_laurea <= 95:
            print("GPA 3.0")
    case voto_laurea if voto_laurea >= 86 and voto_laurea <= 90:
            print("GPA 2.7")
    case voto_laurea if voto_laurea >= 81 and voto_laurea <= 85:
            print("GPA 2.3")
    case voto_laurea if voto_laurea >= 76 and voto_laurea <= 80:
            print("GPA 2.0")
    case voto_laurea if voto_laurea >= 70 and voto_laurea <= 75:
            print("GPA 1.7")
    case voto_laurea if voto_laurea >= 66 and voto_laurea <= 69:
            print("GPA 1.0")
    case _:
            print("Voto non valido")


