'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 

'''

pet1 = {
    'kind': 'dog',
    'owner': 'Lorenzo'
}

pet2 = {
    'kind': 'cat',
    'owner': 'Marcel'
}

pet3 = {
    'kind': 'rabbit',
    'owner': 'Valentina'
}

pet4 = {
    'kind': 'hamster',
    'owner': 'Francesco'
}

pet5 = {
    'kind': 'parrot',
    'owner': 'Leandro'
}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}\n")