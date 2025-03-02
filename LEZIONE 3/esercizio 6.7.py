'''People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.'''


person1:dict[any]={
    "First name":"Lorenzo", 
    "Last name":"Anzivino", 
    "Age": 27, 
    "City" : 
    "Pomezia"
    }
person2:dict[any]={
    "First name":"Patrick", 
    "Last name":"Masone", 
    "Age": 33, 
    "City" : "Pomezia"}
person3:dict[any]= {
    "First name":"Giuseppe", 
    "Last name":"Ciurleo", 
    "Age": 33, 
    "City" : "Roma"}

people:list[dict]= [person1,person2,person3]
    
for person in people:
    print(f"\nFirst Name: {person['First name']}")
    print(f"Last Name: {person['Last name']}")
    print(f"Age: {person['Age']}")
    print(f"City: {person['City']}")
    