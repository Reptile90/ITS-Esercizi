'''Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list'''


cubi: list[int] = []

for numero in range(1, 10):
    cubo = numero ** 3
    cubi.append(cubo)

for cubo in cubi:
    print(cubo)

    print(f"The first three items from in the list are: {cubi[:3]}")
    print(f"Three items from the middle of the list are: {cubi[3:6]}")
    print(f"The last three items in the list are: {cubi[6:9]}")