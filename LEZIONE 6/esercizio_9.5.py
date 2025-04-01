'''Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.'''


class User:
    def __init__ (self,first_name:str, last_name:str, gender:str,hair_colour:str, height:float, job:str,login_attempts:int):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hair_colour = hair_colour
        self.height = height
        self.job = job
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\n Name: {self.first_name} Surname: {self.last_name}, Gender: {self.gender}, Height: {self.height}, Hair Colour: {self.hair_colour}, Job: {self.job}")

    def greet_user(self):
        if self.gender == "Female":
            print (f"Hello girl {self.first_name}, {self.last_name}!")
        elif self.gender == "Male":
            print (f"Hello boy {self.first_name}, {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login resetted. {self.login_attempts}")

utente1 = User("Stefano", "Reali ", "Male", "Brown", "1,93", "Help Desk assistent", 0)

utente1.describe_user()

utente1.greet_user()

utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()
utente1.increment_login_attempts()


utente1.reset_login_attempts()

