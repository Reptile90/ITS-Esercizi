'''9-3. Users: Make a class called User.
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.'''


class User:
    def __init__(self,first_name:str, last_name:str, age:int, height:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self)->None:
        print("USER\n")
        print(f"Name: {self.first_name}\nSurname: {self.last_name}\nAge: {self.age}\nHeight: {self.height} cm")
        print("-"*30)

    def greet_user(self)->None:
        print(f"Hello {self.first_name}. Nice to see you again")
        print("-"*30)



user1 = User("Stefano","Reali",34,193)
user2 = User("Lorenzo", "Anzivino", 28, 180)
user3 = User("Patrick","Masone",33,183)

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()