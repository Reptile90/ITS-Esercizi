'''Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() for each instance.'''

class Restaurant:
    def __init__(self,restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self)->None:
        print(f"We are '{self.restaurant_name}' restaurant and we cook {self.cuisine_type} cuisine")
    

    def open_restaurant(self)->None:
        print(f"The restaurant '{self.restaurant_name}' is open")



restaurant1 = Restaurant("Il Girasole","Chinese")

restaurant2 = Restaurant("Wah Pei", "Chinese")

restaurant3 = Restaurant("Bobbo", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



