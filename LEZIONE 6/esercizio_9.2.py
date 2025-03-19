'''Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.'''

class Restaurant:
    def __init__(self,restaurant_name:str,cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f" The Restaurant {self.restaurant_name} serves {self.cuisine_type}")
       
    def open_restaurant(self):
        print(f" The Restaurant {self.restaurant_name} is open")




restaurant_1 = Restaurant("Il quadrifoglio", "Italian cuisine")
restaurant_2 = Restaurant("Sakura", "Japanese cuisine")
restaurant_3 = Restaurant("Ikku" ,"Chinese cuisine")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
