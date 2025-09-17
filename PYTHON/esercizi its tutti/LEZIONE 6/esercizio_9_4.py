'''Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.'''

class Restaurant:
    def __init__(self,restaurant_name:str,cuisine_type:str,number_served:int = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f" The Restaurant {self.restaurant_name} serves {self.cuisine_type}")
       
    def open_restaurant(self):
        print(f" The Restaurant {self.restaurant_name} is open")

    def incremented_number_served(self):
        self.number_served += 1
        print(f" In this day the restaurant {self.restaurant_name} served {self.number_served} customers")

    def restaurant(self):
        if self.number_served > 0:
            print(f" The Restaurant {self.restaurant_name} served {self.number_served} customers.")
        elif self.number_served == 0:
            print(f"Today the restaurant {self.restaurant_name} doesn't have customers")
        else:
            print("Warning, Error. Number not valid")
    
            
            
