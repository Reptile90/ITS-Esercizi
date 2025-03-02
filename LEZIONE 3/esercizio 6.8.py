'''Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. '''


pet1:dict[str]={
    "Kind":"Cat",
    "Owner":"Stefano"
    }
pet2:dict[str]={
    "Kind":"Dog",
    "Owner":"Lorenzo"
}

pet3:dict[str]= {
    "Kind":"Parrot",
    "Owner": "Marcel"
}

pet4:dict[str]= {
    "Kind":"Rabbit",
    "Owner": "Valentina"
}

pets= [pet1,pet2,pet3,pet4]


for pet in pets:
    print(f"\nPet Kind: {pet['Kind']}")
    print(f"Owner: {pet['Owner']}")
