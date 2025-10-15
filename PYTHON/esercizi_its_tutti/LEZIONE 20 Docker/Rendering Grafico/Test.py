from Quadrato import Quadrato
from Rettangolo import Rettangolo
from Triangolo import Triangolo


quadrato: Quadrato = Quadrato(4)


rettangolo: Rettangolo = Rettangolo(8,4)

triangolo: Triangolo = Triangolo(4)


print(f"L'area del quadrato vale: {quadrato.getArea()}")
quadrato.render()
print()

print(f"L'area del rettangolo vale: {rettangolo.getArea()}")
rettangolo.render()

print()


print(f"L'area del triangolo vale: {triangolo.getArea()}")
triangolo.render()