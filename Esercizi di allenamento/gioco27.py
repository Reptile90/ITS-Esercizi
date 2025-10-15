'''I Rotoli dei Giudici attendono il tuo sigillo: assegna il grado corretto con `grade(score)`, usando soglie **decrescenti**: `A` per `score >= 90`, poi `B` `>= 80`, `C` `>= 70`, `D` `>= 60`, altrimenti `F`. Mantieni la firma e soddisfa i test.'''
from PYTHON.esercizi_its_tutti.DECORATORS.cronometro import cronometro
def grade(score: int) -> str:
    match score:
        case score if score >= 90:
            return "A"
        case score if score >= 80:
            return "B"
        case score if score >= 70:
            return "C"
        case score if score >= 60:
            return "D"
        case default:
            return "F"
        
        
        
        




@cronometro
grade(76)