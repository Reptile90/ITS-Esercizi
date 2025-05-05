'''6-7. People: Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. 
As you loop through the list, print everything you know about each person.'''

person1 = {
    'first_name': 'Lorenzo',
    'last_name': 'Anzivino',
    'age': 27,
    'city': 'Pomezia'
}

person2 = {
    'first_name': 'Patrick',
    'last_name': 'Masone',
    'age': 33,
    'city': 'Pomezia'
}

person3 = {
    'first_name': 'Giuseppe',
    'last_name': 'Ciurleo',
    'age': 33,
    'city': 'Pomezia'
}

people = [person1, person2, person3]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")