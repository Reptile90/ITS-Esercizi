n:int = int(input("Insert Position: "))
match n:
  case 1:
   print(f"You're {n}st")
  case 2:
    print(f"You're {n}nd")
  case 3:
    print(f"You're {n}rd")
  case _:
    print(f"You're {n}th")
