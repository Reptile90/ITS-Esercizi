'''Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time'''


def sandwiches_ingredients(ingredients_list:list[str]):

    for ingredients in ingredients_list:
        print(f"{ingredients}")



cont=0
ingredients_list:list[str] = []
 
while cont < 4:
    choise:str = input("Scegli un ingrediente da aggiungere: ")
    ingredients_list.append(choise)
    cont += 1

sandwiches_ingredients(ingredients_list)
