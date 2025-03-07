'''Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the values that are returned.
'''

def city_country(city:str,country:str)->str : 
    formatted:str = f"{city.capitalize()}, {country.capitalize()}"
    return formatted





print(city_country("roma","italia"))
print(city_country("los angeles", "california"))
print(city_country("stockholm", "sweden"))








































 


