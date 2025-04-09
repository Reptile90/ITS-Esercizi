result = [[x * y for y in range(1, 4)] for x in range(1, 4)]

print(result)

result2 = []
for x in range(1, 4):
    inner_list = []
    for y in range(1, 4):
        inner_list.append(x * y)
    result2.append(inner_list)

print(result2)


x = [1,5]

y = [1,2]

somma = [x[i] + y[i] for i in range (len(x))]

print(somma)