'''No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed'''

username:list[str] = ["Lorenzo ", "Marcel", "Valentina", "Leandro", "Francesco", "admin"] 

if not username:
    print("We need to find some users!")

for name in username:
    if name == "admin":
        print(f"Hello {name} would you like to see a report?")
    else:
        print(f"Hello {name}, thank you for loggin in again")

username.clear()

if not username:
    print("We need to find some users!")
    