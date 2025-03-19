'''Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''


class Restaurant:
    def __init__(self,restaurant_name:str,cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f" The Restaurant {self.restaurant_name} serves {self.cuisine_type}")
       
    def open_restaurant(self):
        print(f" The Restaurant {self.restaurant_name} is open")




restaurant = Restaurant("Il quadrifoglio", "Italian cuisine")

restaurant.describe_restaurant()
restaurant.open_restaurant()


    