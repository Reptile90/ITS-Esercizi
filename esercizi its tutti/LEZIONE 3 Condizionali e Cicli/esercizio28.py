'''6-11. Cities: Make a dictionary called cities.
Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.'''


cities = {
    'rome': {
        'country': 'italy',
        'population': 2860000,
        'fact': 'Rome is known as the Eternal City due to its long history.',
    },
    'paris': {
        'country': 'france',
        'population': 2141000,
        'fact': 'The Eiffel Tower was originally intended to be a temporary structure.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'Tokyo is the most populous metropolitan area in the world.',
    }
}

for key, values in cities.items():
    print(f"\n{key.title()}")
    for key, value in values.items():
        print(f"\t{key.title()}: {value}")