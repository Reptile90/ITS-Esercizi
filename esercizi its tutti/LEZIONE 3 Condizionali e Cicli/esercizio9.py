'''4-10. 
Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.'''

cubo:list[int]= []
for num in range(1,10):
    cubo.append(num**3)

print(cubo)

print(f"The first number is {cubo[:1]}")
print(f"The number in the middle is {cubo[4:5]}")
print(f"The last number are {cubo[-1:]}")
