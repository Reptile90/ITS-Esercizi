sum:int = 0

for i in range (1,11):
    sum+=i
print (f"la somma tra 1 e 10 è {sum}")

sum = 0

for i in range (20,38):
    sum+=i
print(f"la somma tra 20 e 37 è {sum}")

sum = 0
for i in range (35,50):
    sum+=i

print(f"la somma tra 35 e 49 è {sum}")



def sumInRange(a:int,b:int):
    result:int = 0
    for i in range(a,b+1):
        result+=i
    return result

mysum:int = sumInRange(1,10)

print(f"la somma tra 1 e 10 è {sumInRange(1,10)}")


def substract(a:int,b:int):
    result = a - b
    return result


mysubstract:int= substract(10,6)
print(mysubstract)

mysubstract:int = substract(100,32)
print(mysubstract)