'''My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.'''

pizza:list[str] = ["Margherita", "Napoli", "Funghi", "Parmigiana", "Boscaiola"]

friends_pizza:list[str] = pizza.copy()

pizza.append("Patate")
friends_pizza.append("Diavola")


for i in range(len(pizza)):
    print(f"My favorite pizzas are: {pizza[i]}")

for i in range(len(friends_pizza)):
    print(f"My friend’s favorite pizzas are:{friends_pizza[i]}")

