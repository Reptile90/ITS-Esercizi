'''Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.'''



class User:
    def __init__ (self,first_name, last_name, gender,hair_colour, height, job):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hair_colour = hair_colour
        self.height = height
        self.job = job

def describe_user(self):
    print(f"\n Name: {self.first_name} Surname: {self.last_name}, Gender: {self.gender}, Height: {self.height}, Hair Colour: {self.hair_colour}, Job: {self.job}")

def greet_user(self):
    if self.gender == "Female":
        print (f"Hello girl {self.first_name, self.last_name}!")
    elif self.gender == "Male":
        print (f"Hello boy {self.first_name, self.last_name}!")


describe_user("Stefano", "Reali ", "Male", "Brown", "1,93", "Help Desk assistent")

greet_user(describe_user("Stefano", "Reali ", "Male", "Brown", "1,93", "Help Desk assistent"))

