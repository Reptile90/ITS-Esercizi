'''Imported Admin: Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.
'''

class User:
    def __init__(self,first_name:str, last_name:str, username:str, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self)->None:
        print(f"\n Name: {self.first_name} Surname: {self.last_name}, Username: {self.username} Email: {self.email}")

    def greetUser(self)->None:
        print(f" Hello {self.first_name} {self.last_name}")



class Privileges:
    def __init__(self,privileges:list):
        self.privileges = privileges
    
    def showPrivileges(self)->None:
        print("Your priveleges are:")
        for privelege in self.privileges:
            
            print(privelege)
        
