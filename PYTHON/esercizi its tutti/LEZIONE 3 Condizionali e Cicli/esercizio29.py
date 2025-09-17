'''Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.'''

person1 = {
    'first_name': 'Mario',
    'last_name': 'Rossi',
    'age': 35,
    'city': 'Roma',
    'occupation': 'Software Engineer',
    'hobbies': ['Reading', 'Playing guitar', 'Hiking']
}

person2 = {
    'first_name': 'Giulia',
    'last_name': 'Bianchi',
    'age': 28,
    'city': 'Milano',
    'occupation': 'Marketing Specialist',
    'hobbies': ['Traveling', 'Cooking', 'Photography']
}

person3 = {
    'first_name': 'Luca',
    'last_name': 'Verdi',
    'age': 42,
    'city': 'Napoli',
    'occupation': 'Teacher',
    'hobbies': ['Painting', 'Gardening', 'Watching movies']
}

people = [person1, person2, person3]

for person in people:
    print(f"--- {person['first_name'].title()} {person['last_name'].title()} ---")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
    print(f"Occupation: {person['occupation']}")
    print("Hobbies:")
    for hobby in person['hobbies']:
        print(f"- {hobby}")
    print("\n")