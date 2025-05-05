'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live.
You should have keys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.'''


person:dict[str]={}

person["First Name"] = "Lorenzo"
person["Last Name"] = "Anzivino"
person["Age"] = 27
person["City"] = "Pomezia"

for key,value in person.items():
    print(f"{key}:{value}")