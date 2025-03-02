'''Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!'''


favourite_fruits:list [str] =[
    "orange",
    "strawberry",
    "watermelon",

    ]

if "orange" in favourite_fruits:
    print(f"you really like {favourite_fruits[0]}")
if "strawberry" in favourite_fruits:
    print(f"you really like {favourite_fruits[1]}")
if "watermelon" in favourite_fruits:
    print(f"you really like {favourite_fruits[2]}")
