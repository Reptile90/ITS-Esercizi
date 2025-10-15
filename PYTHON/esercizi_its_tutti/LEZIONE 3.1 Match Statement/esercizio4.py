while True:
        try:
            voto_laurea = int(input("Inserisci il voto di laurea: "))
            match voto_laurea:
                case voto if 106 <= voto <= 110:
                    risultato = "GPA 4.0"
                case voto if 101 <= voto <= 105:
                    risultato = "GPA 3.7"
                case voto if 96 <= voto <= 100:
                    risultato = "GPA 3.3"
                case voto if 91 <= voto <= 95:
                    risultato = "GPA 3.0"
                case voto if 86 <= voto <= 90:
                    risultato = "GPA 2.7"
                case voto if 81 <= voto <= 85:
                    risultato = "GPA 2.3"
                case voto if 76 <= voto <= 80:
                    risultato = "GPA 2.0"
                case voto if 70 <= voto <= 75:
                    risultato = "GPA 1.7"
                case voto if 66 <= voto <= 69:
                    risultato = "GPA 1.0"
                case _:
                    risultato = "Voto non valido"
            print(f"Output: {risultato}")
            break
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")