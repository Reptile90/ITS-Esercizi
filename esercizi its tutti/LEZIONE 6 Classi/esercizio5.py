'''Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.
'''


class User:
    def __init__(self,first_name:str, last_name:str, age:int, height:int,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempt = 0

    def describe_user(self)->None:
        print("USER\n")
        print(f"Name: {self.first_name}\nSurname: {self.last_name}\nAge: {self.age}\nHeight: {self.height} cm")
        print("-"*30)

    def greet_user(self)->None:
        print(f"Hello {self.first_name}. Nice to see you again")
        print("-"*30)

    def increment_login_attempt(self)->int:
        self.login_attempt += 1
        return f"Login {self.login_attempt}"
    
    def reset_login_attempt(self)->int:
        self.login_attempt = 0
        return f"Login {self.login_attempt}"


user1 = User("Stefano","Reali",34,193)
user2 = User("Lorenzo", "Anzivino", 28, 180)
user3 = User("Patrick","Masone",33,183)

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()


print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())
print(user1.increment_login_attempt())

print(user1.reset_login_attempt())